#include <iostream>
#include <queue>
using namespace std;

int main(){
int N;
cin >> N;
for (int I = 1; I <= N; ++I){
string s;
int n;
int d = 0;
cin >> s >> n;
vector<int> v(s.size());
queue<int> q;
int p=0;
for(int i = 0; i < s.size(); ++i){
if(s[i] == '+' and p == 1) {
q.push(i+n-1);
p = 1-p;
++d;
}
if(s[i] == '-' and p == 0){
q.push(i+n-1);
p = 1-p;
++d;
}
if(q.size() and q.front()==i){
q.pop();
p = 1-p;
}
}
if(q.size()) cout << "Case #" << I << ": IMPOSSIBLE" << endl;
else cout << "Case #" << I << ": " << d << endl;
}
}
