### pipeline idea
1. I want CameraClipPreview, it's supported by my hw
1. get that from CameraMotion (also supported)
this will have eventSessionId, which gets associated back to CameraClipPreview
1. we can get CameraMotion event by subscribing:
https://developers.google.com/nest/device-access/subscribe-to-events


### access
- I got things configured and basic curl works, `google-nest-sdm` works too
- but I can only get this going for listing devices, I'm having trouble subscribing


### on the oauth tokens, refreshes and more
https://developers.google.com/nest/device-access/authorize#how_to_use_a_refresh_token

for setting up the redirect URI, trailing slashes matter..


### doorbell capabilities
https://developers.google.com/nest/device-access/api/doorbell-wired


### similar projects
https://medium.com/@tamirmayer/google-nest-camera-internal-api-fdf9dc3ce167
https://github.com/potmat/homebridge-google-nest-sdm
https://developers.google.com/nest/device-access/samples/web-app


### webhook
```
$ gcloud functions deploy webhook --runtime python39 --trigger-http --allow-unauthenticated --source=./webhook-handler
$ gcloud alpha logging tail "resource.type=cloud_function AND resource.labels.function_name=webhook"
```

on setting up live tailing for the gcloud function (webhook testing):
https://til.simonwillison.net/cloudrun/tailing-cloud-run-request-logs


### consoles
- https://console.nest.google.com/device-access
- https://console.cloud.google.com/


### next steps
I don't think you're getting a correct SDP response, could try to generate one from the webapp example
for instance this line:

```
...
m=audio 19305 UDP/TLS/RTP/SAVPF 96
c=IN IP4 172.217.198.127
...
m=video 9 UDP/TLS/RTP/SAVPF 101 102
c=IN IP4 0.0.0.0
...
```
means it's trying to send video over 0.0.0.0:9 which is not going to work..it's too low/going to be used
interestingly though the audio seems to be setup correctly..j
also IDK why the offer SDP from sdp.py "proposes" some ports which the answer seems to show the device has rejected?


also still not getting events from the camera (just thermostat)..sadly..may need to fully re-setup the integration? Tamir's project had same issue, sporadic delivery
