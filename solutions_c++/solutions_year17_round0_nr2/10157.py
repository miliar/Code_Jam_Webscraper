#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        int n;
        cin>>n;
        for(int j=n;j>=1;j--){
            int count=0;
            int a=j;
            while(a>0){
                count++;
                a/=10;
            }
            a=j;
            int count1=0;
            int b;
            int count2=count-1;
            while(count2!=0){
                b=a%10;
                a/=10;
                if(b>=(a%10))
                    count1++;
                    count2--;
            }
                        if(count1==count-1){
                cout<<"Case #"<<i<<": "<<j<<endl;
                break;
        }
    }
    }
    return 0;
}
