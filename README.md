# AI Predictive Medic

Watch The Working First

[![Watch the video](https://img.youtube.com/vi/4uHltV9FMYE/hqdefault.jpg)](https://www.youtube.com/watch?v=4uHltV9FMYE)

Think about all the machines you use during a year, all of them, from a toaster every morning to an airplane every summer holiday. Now imagine that, from now on, one of them would fail every day. What impact would that have? The truth is that we are surrounded by machines that make our life easier, but we also get more and more dependent on them. Therefore, the quality of a machine is not only based on how useful and efficient it is, but also on how reliable it is. And together with reliability comes maintenance.

When the impact of a failure cannot be afforded, such as a malfunctioning airplane engine, the machine should be subjected to preventive maintenance. Maintenance becomes a tedious process with increase in complexity of the machine, with many components working together influencing each others' lifetime. In such a system how can one predict the right moment for maintenance so that the components are not prematurely but the whole machine works reliable. There arises the importance of preventive maintenance.

In this solution we collect all the possible data of a machine. Using the Brainium widgets and Machine learning algorithms the collected data is processed. The collected data with historic characteristics can be used for predictive maintenance.

Consider a machine say, a motor. We can find all the properties like temperature, vibrations, magnetic field, sound intensity etc produced by motor using sensors on the SmartEdge Agile board. The data is directly passed and processed by Brainium portal widgets. Using the historical and static characteristics one can choose any one of following the predictive maintenance strategies.

1. Regression models to predict remaining useful lifetime (RUL) : Based on the historic characteristics of the system and on how it behaves now (static characteristics), the remaining useful time can be predicted. Assuming the degradation process to be smooth.

2. Classification models to predict failure within a given time window: In this strategy the data needed are more or less same. But the major difference is that since we are defining a time window the degradation process shouldn't be smooth.

3. Flagging anomalous behavior: If the degradation process is very rapid or there are too many types of failures or there are only a few failure data we define the collected data under normal conditions to be normal and any change in normal behavior is notified.

In our solution we use historical data and define it to be normal behavior. And whenever a violation from this behavior is noted the maintenance team is notified. The team can visualize the current data and historical data and can compare and analyze the behavior and necessary maintenance can be taken to avoid failures.

Using the historical data and the live data we can detect,

1. Normal Working Mode
2. Irregular vibrations (due to unbound screws or anything similar)
3. Heating Issues (due to internal short circuits or anything similar)

Also by collecting the parameters of motor like temperature,magnetic field, sound pattern and by processing them using ML algorithms we can predict the next expected maintenance time to a good extent.

## HardWare SetUp
As stated earlier we are using an AC motor operating at 220V. A motor is a basic part of any of large machineries so the elemental motor is a good case study.

![AC Motor for study](https://hackster.imgix.net/uploads/attachments/982710/uploads2ftmp2ff8bb06dc-9d5d-4046-adc0-55f7f7865f362fe91a6150_gGNkiJWCmK.JPG?auto=compress%2Cformat&w=740&h=555&fit=max "AC Motor")

![Brainium](https://hackster.imgix.net/uploads/attachments/982712/uploads2ftmp2fc3b633ea-433b-4387-83f4-638dbd355b612fe91a6145_Dv2zDD7Mo6.JPG?auto=compress%2Cformat&w=740&h=555&fit=max "SmartEdge Agile")

We mount SmartEdge Agile on the motor and fix it firmly.

![Experimental Setup](https://hackster.imgix.net/uploads/attachments/982711/uploads2ftmp2fabb20c6f-e21f-4719-92ed-112b051d31312fe91a6154_ArmWuHcxgf.JPG?auto=compress%2Cformat&w=740&h=555&fit=max "Experimental Setup")

We use Raspberry Pi as the output UI for users to analyse the machine. The python program running in Raspberry Pi collects data from brainium portal and processes it and enable users to analyse the machineWe use Raspberry Pi as the output UI for users to analyse the machine.

## Software
### Getting Started With Brainium

To use our SmartEdge Agile device, first we need o create an account on the [Brainium platform](https://brainium.com). The we can download the Brainium Gateway companion app to our phone and use our newly created account to log into it. The phone will act as a gateway, between the Brainium Portal and our AI devices connected over Bluetooth.

![](https://hackster.imgix.net/uploads/attachments/982716/uploads2ftmp2f47708d8a-269a-41a0-a8d3-a267096b1ccd2fphoto_2019-08-23_22-05-32_GAWM810JUk.jpg?auto=compress%2Cformat&w=740&h=555&fit=max "GATEWAY")


![](https://hackster.imgix.net/uploads/attachments/982735/uploads2ftmp2ff3666441-9d98-45ed-a232-be40d7e667382fbc_1OjgPWz706.png?auto=compress%2Cformat&w=740&h=555&fit=max "ALL CONNECTED DEVICES WILL SHOW UP HERE")

### Predictive Maintenance

After setting up brainium gateway let's build a new project. Then go to PdM panel and create a new PdM workspace

![](https://hackster.imgix.net/uploads/attachments/982738/uploads2ftmp2fcab09243-38a4-429a-a05b-b21d0ef1bf912fbd_WCV9qngWtT.png?auto=compress%2Cformat&w=740&h=555&fit=max "PdM Wrokspace")

### Initial Learning stage

In this stage the platform tries to learn how our device normally operates. It tries to identify stationary(states) and dynamic(transitions between states)patterns, based on the sensor data of the SmartEdge Agile.

In our case we have mainly 3 normal states

1. Turning On
2. Normal Working Mode
3. Turning Off

Also we have added certain other patterns that may be generated during working such as vibration pattern with unbound or loose screws, vibrations with something stuck inside motor etc.

![](https://hackster.imgix.net/uploads/attachments/982741/uploads2ftmp2f5905907b-9ae4-4685-9566-048667da62062fpattern_28229_IvRJcM1OCz.jpg?auto=compress%2Cformat&w=740&h=555&fit=max "Patterns")

Once we have got enough data patterns let's generate the model and apply it to SmartEdge Agile.

### Continuous Learning stage

In this stage the portal keeps on learning new patterns to get a complete knowledge about working of our device. The more patterns we detect the more accurate will be the prediction.

### Rules and Alerts

After the application of model to the device we want to enforce certain rules for the portal to respond. We can have two type of rules

### AI rules
AI rules are those rules that can be applied for motion recognition and PdM. In our project we enforce certain rules. According to these rules the portal produce alerts.

### Normal rules
AI rules are those rules that can be applied for sensors. In our project we enforce certain rules. According to these rules the portal produce alerts.

![](https://hackster.imgix.net/uploads/attachments/982743/uploads2ftmp2f762b1d26-a2ec-472f-b149-5bddd98dc8922fdashboard28229_2HUZRwOuOU.jpg?auto=compress%2Cformat&w=740&h=555&fit=max "Dashboard")

#### MQTT over WebSocket API

MQTT API provides access to the data which has been sent from user's devices in real-time.

#### How to connect

MQTT API is available over WebSockets by the following URI: wss://ns01-wss.brainium.com and it's secured. The MQTT protocol provides username and password fields in the CONNECT message for authentication. The client has the option to send a username and a password when it connects to an MQTT broker. For connection to Brainium Platform this option is a must:

the username has the specified static value : oauth2-user
the password is different for each user and equals to external access token (it's available in the user's profile).


### Python Code

We run this python code in Raspberry Pi which waits for alerts to be triggered in the brainium portal. When alert is triggered we get the value in the program. After the value is received, the program checks for anomalous(faulty behaviour) PdM pattern and if any triggers an alert in android application or any other suitable UI. Also the sensors data are saved into cloud for further processing. From the sensory data by using ML algorithms time before next failure can be approximated.
The more details about how to use python code is described [here](Python)

### Mobile App

We are providing a Mobile app that enables users to analyse the machine. Find more details [here](Android)


