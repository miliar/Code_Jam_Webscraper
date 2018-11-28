#include<bits/stdc++.h>
using namespace std;

vector<pair<int,double> > V;

int next[100010]={-1};

int find_next(int i,double& curS){

if(next[i]==-1)
    return next[i];

  if(V[next[i]].second < curS)
    return next[i];

    return find_next(next[i],curS);
}

int main()
{
    freopen("in12.txt","r",stdin);
    freopen("out12.txt","w",stdout);
    int t,t1=1;
    scanf("%d",&t);
    while(t--)
    {

        printf("Case #%d: ",t1++);
        double D;
        int N;
        cin>>D>>N;
        for(int i=0;i<N;++i)
        {
            int P;
            double S;
            cin>>P>>S;
            V.push_back(make_pair(P,S));
        }
        sort(V.begin(),V.end());
        for(int i=N-1;i>=0;--i){
            if(i==N-1)
            next[i]=-1;
            else{

                double curS= V[i].second;
                if(curS>V[i+1].second)
                    next[i]=i+1;
                else{
                    next[i]=find_next(i+1,curS);
                }
            }
        }

        double maxTime=-1;
        double speed;

        for(int i=0;i<N;++i){

           if(next[i]==-1){

            double tm= (D-V[i].first)/V[i].second;

            if(tm>maxTime){
                maxTime=tm;
                speed = D/tm;
            }
           }
           else{

            double tm1= (V[next[i]].first-V[i].first)/(V[i].second-V[next[i]].second);

            double tm2 = (D-V[next[i]].first)/V[next[i]].second;

            if(tm1<tm2) // catches the slower one
            {
               //do nothing..

            }
            else{

                double tm = (D-V[i].first)/V[i].second;
                if(tm>maxTime){
                maxTime=tm;
                speed = D/tm;
                }
            }
        }
    }
   V.clear();
   //cout<<speed<<endl;
   printf("%.6f\n",speed);

  }

    return 0;
}
