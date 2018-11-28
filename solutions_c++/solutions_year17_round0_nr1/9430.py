#include<iostream>
#include<vector>
using namespace std;
int main()
{
int T,K,count=0;
string S;
vector<int> a;
cin>>T;
while(T--)
{    cin>>S;
    cin>>K;
    count=0;
    for(int i=0;i<=S.size()-K;i++)
    {
        if(S.at(i)=='-')
        {
            for(int j=0;j<K;j++)
             {
            if(S.at(j+i)=='+')
                {
                S.at(j+i)='-';
                }
            else
                S.at(j+i)='+';
             }
          count++;
        }


}
 for(int i=S.size()-K+1;i<S.size();i++)
      {
          if(S.at(i)=='-')
            count=-1;
      }
if(count==-1)
    a.push_back(-1);
else
 a.push_back(count);

}
for(int i = 0; i < a.size(); i++){
    cout<<"Case #"<<i+1<<": ";
    if(a.at(i) == -1){
        cout<<"IMPOSSIBLE"<<endl;
    }
else{
    cout<<a.at(i)<<endl;
}
}

}
