#include<bits/stdc++.h>
using namespace std ;

multiset<int> p;

int main()
{
// freopen("C-small-2-attempt4.in","r",stdin);
//   freopen("C-outuput2.txt","w",stdout);
    int t,n,k,ans,m,con=0;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
         con=0;
        p.clear();
        ans=0;
        cin>>n>>k;
        p.insert(n);
         for (std::multiset<int>::reverse_iterator  it=p.rbegin(); it!=p.rend(); ++it)
        {
            con++;
            if(con==k)
            {
                con=*it;
                break;
            }
              if(*it%2==0)
              {
                  p.insert((*it/2.0)-1);
              }
              else
              {
                  p.insert((*it/2.0));
              }
              p.insert((*it/2.0));

        }


        cout<<"Case #"<<o<<": ";
        if(con==1 || con%2)
        {
            con=con/2;
            cout<<con<<" "<<con<<endl;
        }
        else
        {
            con=con/2;
            cout<<con<<" "<<con-1<<endl;
        }
    }
}
