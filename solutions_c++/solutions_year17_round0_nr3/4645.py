#include<bits/stdc++.h>
using namespace std;

int main() {
 // your code goes here
 freopen("C:\\Users\\hp\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\hp\\Desktop\\output.txt","w",stdout);
int t;
cin>>t;
int z=1;
while(t--)
{
 int n,k;
 cin>>n>>k;
 priority_queue<int> q;
 q.push(n);
 int curr;
 while(k--)
 {
  curr=q.top();
  q.pop();
  int x=(curr-1)/2;
  int y=(curr/2);
  q.push(x);
  q.push(y);
 }
 cout<<"Case #"<<z++<<": "<<(curr/2)<<" "<<(curr-1)/2<<endl;

}
 return 0;
}
