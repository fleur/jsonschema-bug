import os
import json
import jsonschema


schemas_dict = { }
type_hierarchy_dict = None


# reads in all json schemas from the 'schemas' directory
# puts them in a dict, indexed by title
for filename in [each for each in os.listdir('schemas') if each.endswith('.json')]:
    path = os.path.join('schemas', filename)
    print "reading schema:", path

    with open(path) as json_data:
        tmp = json.load(json_data)
        if (tmp['properties'].has_key('type')):
            schemas_dict[tmp['title']] = tmp

schema_types = schemas_dict.keys()


def validate(data):

    try:
        uri = 'file://'+os.path.join(os.getcwd(), 'schemas')
        print "uri:", uri
        r = jsonschema.RefResolver(uri, None)
        v = jsonschema.Draft4Validator(schemas_dict[data['type']], resolver=r)
        v.validate(data)

    except jsonschema.exceptions.ValidationError as e:
        msgs = [e.message]

        errors = sorted(v.iter_errors(data), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                msgs.append(suberror.message)

        raise TypeError(msgs)
        
    return data

if __name__ == "__main__":

    validate({'type': 'project'})
