#include<bits\stdc++.h>
using namespace std;
void __main(int test){
    double max_time=-1;
    double D;
    int N;
    cin>>D>>N;
    for(int i=0;i<N;i++){
        double HP,HS;
        cin>>HP>>HS;
        max_time=max((D-HP)/HS,max_time);
    }
    printf("%f",D/max_time);
}
int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        cout<<"Case #"<<t<<": ";
        __main(t);
        cout<<endl;
    }
    return 0;
}

