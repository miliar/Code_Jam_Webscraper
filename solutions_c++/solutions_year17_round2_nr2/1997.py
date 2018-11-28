#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;

	int n,R,O,Y,G,B,V;


	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<": ";

        cin>>n;

        cin>>R>>O>>Y>>G>>B>>V;


        bool ck=true;

        if((Y+B)>=R && (Y+R)>=B && (B+R)>=Y)
            ck=true;
        else
            ck=false;


        if(!ck)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

       vector<pair<int,char> >  vc;

       vc.push_back(make_pair(R,'R'));
       vc.push_back(make_pair(Y,'Y'));
       vc.push_back(make_pair(B,'B'));
       sort(vc.begin(),vc.end());

       if(vc[0].first+vc[1].first==vc[2].first)
       {
           for(int i=0;i<vc[2].first;i++)
           {
               cout<<vc[2].second;

               if(vc[1].first)
               {
                   vc[1].first--;
                   cout<<vc[1].second;
               }
               else
               {
                   vc[0].first--;
                   cout<<vc[0].second;
               }
           }
           cout<<endl;
       }
       else
       {
           int rem = (vc[0].first+vc[1].first-vc[2].first);

            int i;
           for(i=0;i<rem;i++)
           {
               cout<<vc[2].second;
               cout<<vc[0].second; vc[0].first--;
               cout<<vc[1].second;  vc[1].first--;
           }

           for(int j=i;j<vc[2].first;j++)
           {
               cout<<vc[2].second;

               if(vc[1].first)
               {
                   vc[1].first--;
                   cout<<vc[1].second;
               }
               else
               {
                   vc[0].first--;
                   cout<<vc[0].second;
               }
           }

           cout<<endl;
       }



	}
}
