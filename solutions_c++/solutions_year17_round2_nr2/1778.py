#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{

    freopen("B-small-attempt2.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int x=1;x<t+1;x++){

        int n,red,orange,yellow,green,blue,violet;
        cin>>n>>red>>orange>>yellow>>green>>blue>>violet;
        cout<<"Case #"<<x<<": ";
        if((red==0||yellow==0||blue==0)&&(red+yellow+blue)%2!=0)cout<<"IMPOSSIBLE"<<endl;
        else if(2*max(red,max(yellow,blue))>n){cout<<"IMPOSSIBLE"<<endl;}
        else{
            int large,mid,small;
            char largeC,midC,smallC;
            if(red>=yellow&&red>=blue){
                large=red;largeC='R';
                if(blue>=yellow){mid=blue;midC='B';small=yellow;smallC='Y';}
                else{mid=yellow;midC='Y';small=blue;smallC='B';}
            }
            else if (blue>=yellow&&blue>=red){
                large=blue;largeC='B';
                if(red>=yellow){mid=red;midC='R';small=yellow;smallC='Y';}
                else{mid=yellow;midC='Y';small=red;smallC='R';}
            }
            else{
                large=yellow;largeC='Y';
                if(red>=blue){mid=red;midC='R';small=blue;smallC='B';}
                else{mid=blue;midC='B';small=red;smallC='R';}
            }


            if(mid+small>large){
                for (int i=0;i<large-small;i++)cout<<largeC<<midC;
                for(int i=0;i<mid+small-large;i++)cout<<largeC<<midC<<smallC;
                for(int i=0;i<large-mid;i++)cout<<largeC<<smallC;
            }
            else if(large==small){
                for(int i=0;i<small;i++)cout<<largeC<<midC<<smallC;
            }
            else{
                for(int i=0;i<mid;i++)cout<<largeC<<midC;
                for(int i=0;i<small;i++)cout<<largeC<<smallC;
            }
        cout<<endl;
        }
    }
    return 0;
}
