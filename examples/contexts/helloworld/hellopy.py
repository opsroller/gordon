import json

print('Loading function')


def handler(event, context):
    with open('.context', 'r') as f:
        gordon_context = json.loads(f.read())

    print(unicode(gordon_context))
    return gordon_context['bucket']
