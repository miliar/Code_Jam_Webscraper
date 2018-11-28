#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> P;
typedef pair<P,int> PP;


char getM(int p){
  if(p==0)return 'R';
  if(p==2)return 'Y';
  if(p==4)return 'B';
}

int main(){
  int T;
  cin>>T;
  for(int q=1;q<=T;q++){
    int a[6],n,f=0;
    string ans;
    cin>>n;
    for(int i=0;i<6;i++)cin>>a[i];
    if(max(a[0],max(a[2],a[4]))<=(n)/2){
      priority_queue<PP> Q;
      P b[3];
      b[0]=P(a[0],0);
      b[1]=P(a[2],2);
      b[2]=P(a[4],4);
      sort(b,b+3);
      reverse(b,b+3);

      ans+=getM(b[0].second),a[b[0].second]--;

      int y=b[0].second;
      if(a[0])Q.push(PP(P(a[0],-abs(0-y)),0));
      if(a[2])Q.push(PP(P(a[2],-abs(2-y)),2));
      if(a[4])Q.push(PP(P(a[4],-abs(4-y)),4));
      while(!Q.empty()){
	PP tp=Q.top();Q.pop();
	if(ans.size()&&ans[ans.size()-1]==getM(tp.second)){
	  PP tp1=Q.top();Q.pop();
	  ans+=getM(tp1.second);
	  if(tp1.first.first-1)
	    Q.push(PP(P(tp1.first.first-1,tp1.first.second),tp1.second));
	  Q.push(PP(P(tp.first.first,tp.first.second),tp.second));
	}
	else {
	  ans+=getM(tp.second);
	  if(tp.first.first-1)
	    Q.push(PP(P(tp.first.first-1,tp.first.second),tp.second));
	}
      }
      f=1;
    }
    cout<<"Case #"<<q<<": ";
    if(f)cout<<ans<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }

  return 0;
}
/*
R,Y,B;
O=R+Y;
G=Y+B;
V=R+B;		      
*/
