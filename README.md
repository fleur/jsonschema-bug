
The project schema inherits from the container schema, which inherits from the generic schema.

The JSON schema files are all located in the same directory.

Run:

	python validate.py



Note line 7 of container:

    "allOf": [ { "$ref": "file:schemas/generic.json" } ],



And line 7 of project.json:

    "allOf": [ { "$ref": "file:schemas/container.json" } ],



If you change line 7 of container.json to this, and only container.json, NOT project.json, it works as expected (which is the schema validation fails with the required property of 'name' missing):

    "allOf": [ { "$ref": "file:generic.json" } ],
