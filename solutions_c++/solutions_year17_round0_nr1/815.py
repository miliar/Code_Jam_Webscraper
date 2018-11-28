#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;


int main(){
	ifstream inf("A-large.in");
    int n;
    inf>>n;
    string t;
    int b;
    int x=1;
    while(n--){
    	cout<<"Case #"<<x<<": ";
    	x++;
        inf>>t;
        inf>>b;
        int r = 0;
        for(int i = b;i<t.size();i++){
            if(t[i-b]=='-'){
                r++;
                for(int j = i-b;j<i;j++){
                    if(t[j]=='-')
                        t[j] = '+';
                    else
                        t[j] = '-';
                }
            }
        }
        int sb = t.size()-b;
        bool k = 0;
        for(int i = t.size()-b;i<t.size();i++){
            if(t[i]!=t[sb]){
                cout<<"IMPOSSIBLE"<<endl;
                k = 1;
                break;
            }
        }
        if(k)
            continue;
        if(t[sb]=='-')
            r++;
        cout<<r<<endl;
    }

    return 0;
}
