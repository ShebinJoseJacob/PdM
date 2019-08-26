# AI Predictive Medic
Think about all the machines you use during a year, all of them, from a toaster every morning to an airplane every summer holiday. Now imagine that, from now on, one of them would fail every day. What impact would that have? The truth is that we are surrounded by machines that make our life easier, but we also get more and more dependent on them. Therefore, the quality of a machine is not only based on how useful and efficient it is, but also on how reliable it is. And together with reliability comes maintenance.

When the impact of a failure cannot be afforded, such as a malfunctioning airplane engine, the machine should be subjected to preventive maintenance. Maintenance becomes a tedious process with increase in complexity of the machine, with many components working together influencing each others' lifetime. In such a system how can one predict the right moment for maintenance so that the components are not prematurely but the whole machine works reliable. There arises the importance of preventive maintenance.

In this solution we collect all the possible data of a machine. Using the Brainium widgets and Machine learning algorithms the collected data is processed. The collected data with historic characteristics can be used for predictive maintenance.

Consider a machine say, a motor. We can find all the properties like temperature, vibrations, magnetic field, sound intensity etc produced by motor using sensors on the SmartEdge Agile board. The data is directly passed and processed by Brainium portal widgets. Using the historical and static characteristics one can choose any one of following the predictive maintenance strategies.

1 Regression models to predict remaining useful lifetime (RUL) : Based on the historic characteristics of the system and on how it behaves now (static characteristics), the remaining useful time can be predicted. Assuming the degradation process to be smooth.

2 Classification models to predict failure within a given time window: In this strategy the data needed are more or less same. But the major difference is that since we are defining a time window the degradation process shouldn't be smooth.

3 Flagging anomalous behavior: If the degradation process is very rapid or there are too many types of failures or there are only a few failure data we define the collected data under normal conditions to be normal and any change in normal behavior is notified.

In our solution we use historical data and define it to be normal behavior. And whenever a violation from this behavior is noted the maintenance team is notified. The team can visualize the current data and historical data and can compare and analyze the behavior and necessary maintenance can be taken to avoid failures.

Using the historical data and the live data we can detect,

1 Normal Working Mode
2 Irregular vibrations (due to unbound screws or anything similar)
3 Heating Issues (due to internal short circuits or anything similar)

Also by collecting the parameters of motor like temperature,magnetic field, sound pattern and by processing them using ML algorithms we can predict the next expected maintenance time to a good extent.

##HardWare SetUp
As stated earlier we are using an AC motor operating at 220V. A motor is a basic part of any of large machineries so the elemental motor is a good case study.
