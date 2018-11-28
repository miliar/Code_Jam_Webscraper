#include <bits/stdc++.h>
using namespace std;
typedef pair<string,int> pii;
int k,n;

void flip(char &str,int &nop) {
if(str=='+') { str='-';nop--; }
else { str='+';nop++; }
}

int sfp(string str) {
int nop=0;

for(int i=0;i<n;i++)
if(str[i]=='+')
nop++;

int i;
queue<pii > q;
queue<int > step;
map<string,int>mp;
int cstep;

q.push(pii(str,nop));
step.push(0);

while(!q.empty()) {
pii temp = q.front();
q.pop();
str = temp.first;
nop = temp.second;
mp[str] = step.front();
cstep = step.front();
step.pop();
//cout<<str<<" "<<nop<<" "<<cstep<<" "<<n<<endl;
if(nop==n) return cstep;

for(i=0;i<k;i++) {
flip(str[i],nop);
}

if(!mp.count(str)) {
q.push(pii(str,nop));
step.push(cstep+1);
}

for(i=1;i<n-k+1;i++) {
flip(str[i-1],nop);
flip(str[i+k-1],nop);
if(!mp.count(str)) {
q.push(pii(str,nop));
step.push(cstep+1);
}

}



}


return -1;

}


int main() {

ifstream cin("input.txt");
ofstream cout("output.txt");

int nop=0;
int t,test=0;
cin>>t;

while(t--) {

string str;
cin>>str>>k;
n = str.length();
int result = sfp(str);
if(result==-1)
cout<<"Case #"<<(++test)<<": "<<"IMPOSSIBLE"<<endl;
else
cout<<"Case #"<<(++test)<<": "<<result<<endl;

}
return 0;
}
