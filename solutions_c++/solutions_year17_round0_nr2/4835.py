#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL

int main()
{
   int t;
   cin>>t;
   int y=0;
   while(t--){
       y++;
      ll n;
      cin>>n;
      stack< int > st;
      while(n){
        int te= n%10;
        n/=10;
        st.push(te);
      }
      int A[st.size()];
      int i=0;
      int sz=st.size();
      while(st.size()){
        A[i++]=st.top();
        st.pop();
      }
       int borrow=0;
       int idx;
      while(true){
          if(borrow){ if(A[idx]){ A[idx]--;borrow=0;  }else{ A[idx]=9; continue; }}
          int ind=-1;
          int f=0;
         for (int i = 1; i <sz; ++i)
         {
            if(A[i]<A[i-1] and !f){
               ind=i-1;
               f=1;
               i--;
            }
            else if(f){
              A[i]=9;
            }
         }
         if(ind==-1){ break;}
         else{ idx= ind; borrow=1; }
      }
       cout<<"Case #"<<y<<": ";
       for (int i = 0; i <sz; ++i)
       {
         if(A[i]){ cout<<A[i];}
       }
       cout<<endl;
   }
  return 0;
}