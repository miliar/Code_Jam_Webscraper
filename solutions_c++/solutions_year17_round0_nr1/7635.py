#include <iostream>
#include <cstdio>
using namespace std;
int t,k,l,res,flips;
string s;
int arr[1005];
int main()
{
    freopen("entrada.in","r",stdin);
    freopen("salida.out","w",stdout);
    cin>>t;
    for (int caso=1;caso<=t;caso++){
        cin>>s>>k;
        res=0;
        flips=0;
        l = s.size();
        for (int i=0;i<l;i++)
            arr[i]=0;
        for (int i=0;i<l && res>=0;i++){
            flips+=arr[i];
            if ((s[i]=='-' && flips%2==0) || (s[i]=='+' && flips%2==1)){
                if (i+k<=l){
                    flips++;
                    arr[i+k]--;
                    res++;
                }
                else
                    res=-1;
            }
        }
        cout<<"Case #"<<caso<<": ";
        if (res<0)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<res<<endl;
    }
    return 0;
}
