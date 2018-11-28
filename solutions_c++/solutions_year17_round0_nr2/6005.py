#include<bits/stdc++.h>
#include <string>

using namespace std;
#include <sstream>

template <typename T>
std::string NumberToString ( T Number ){std::ostringstream ss;ss << Number;return ss.str();}
typedef long long ll;

int arr[20];
int main()
{
    freopen("in.txt.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int tt=0;
    while(t--){
        cout<<"Case #"<<++tt<<": ";
        string a;
        cin>>a;
        for(int i=0;i<a.length();i++){
            arr[i]=a[i]-'0';
        }
        int n=a.length()-1;
        int last = n;
        while(n>0){
            if(arr[n]<arr[n-1]){
                arr[n]=9;
                arr[n-1]--;
                last=n;
            }
            n--;
        }
        int st=0;
        if (arr[0]==0)
            st++;
        for(;st<a.length();st++){
            if(st>last){
                cout<<"9";
                continue;
            }
            cout<<arr[st];
        }
        cout<<endl;

    }
}
