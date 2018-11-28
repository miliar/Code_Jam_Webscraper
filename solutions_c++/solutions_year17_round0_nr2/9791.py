#include <iostream>

using namespace std;
typedef long long ll;
int main()
{
    char s[1000000];
    ll T;
    cin>>T;
	ll num;
    for(num=1;num<=T;num++){
    cin>>s;
	cout<<"Case #"<<num<<": ";
    ll i;
    for(i=0;s[i+1]!='\0';){
        if(s[i]<s[i+1]){
            cout<<s[i];
            i++;
        }
        else if(s[i]==s[i+1]){
            ll j=i;
            while(s[j]!='\0'&&s[j+1]!='\0'&&s[j]<=s[j+1]){
            j++;
        }
        if(s[j+1]=='\0'){
            while(s[i]!='\0'){
                cout<<s[i];
                i++;
            }
        }else{
            cout<<(char)(s[i]-1);
            i++;
            while(s[i]!='\0'){
                cout<<"9";
                i++;
            }

        }
        }else{
            if(i==0&&(char)(s[i]-1)=='0'){
            }else{
                cout<<(char)(s[i]-1);
                }
            i++;
            while(s[i]!='\0'){
                cout<<"9";
                i++;
            }
        }
    }

    if(s[i]!='\0'&&s[i+1]=='\0'){
        cout<<s[i];
    }
    cout<<endl;
    }
    return 0;
}
