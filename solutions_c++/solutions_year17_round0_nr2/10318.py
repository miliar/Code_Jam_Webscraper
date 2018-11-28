#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;
typedef unsigned long long ull;
#define psb push_back
#define mkp make_pair
#define all(x) (x).begin(),(x).end()
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
int toint(string x)
{
    istringstream ss(x);
    int a;
    ss>>a;
    return a;
}
string tostr(int x)
{
    ostringstream ss;
    ss<<x;
    return ss.str();
}
bool istidy(int x){
    if(x<10){return true;}
    else{
        bool res=true;
        string s=tostr(x);
        int i=0;
        while(i<s.length()-1&&res){
            if(toint(s.substr(i,1))>toint(s.substr(i+1,1))){
                res=false;
            }
            i++;
        }
        return res;
    }
    
}
int main() {
	// your code goes here
	int n,tmp;
        cin>>n;
        for(int i=1;i<=n;i++){
            cin>>tmp;
            while(!istidy(tmp)){
                tmp--;
            }
            cout<<"Case #"<<i<<": "<<tmp<<"\n";
        }
	return 0;
}
