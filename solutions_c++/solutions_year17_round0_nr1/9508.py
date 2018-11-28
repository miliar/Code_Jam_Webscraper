#include <iostream>
#include <string>
#include<fstream>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("op1.out","w",stdout);
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++){
        string s;
        int k;
        int count = 0;
        cin>>s>>k;
        int x = 0,y = k-1,j;
        while(y < s.length()){
            if(s[x] == '-'){
                count++;
                for(j = x;j<=y;j++){
                    if(s[j] == '-')
                    s[j] = '+';
                    else
                    s[j] = '-';
                }
            }
            x++;
            y++;
        }

            bool found = true;
            for(j=0;j<s.size();j++){
                if(s[j] == '-'){
                    found = false;
                    cout<<"Case #"<<i<<": "<<"IMPOSSIBLE";
                    break;
                }
            }
            if(found){
                cout<<"Case #"<<i<<": "<<count;
            }
        cout<<endl;
    }
    
	return 0;
}

