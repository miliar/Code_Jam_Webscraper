#include<bits/stdc++.h>
using namespace std;

int main()
{


freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int curr=1;
    int t;
    cin>>t;
    while(t--)
    {

        int n,a,o,b,g,c,v;
        cin>>n>>a>>o>>b>>g>>c>>v;
        bool imp=false;
        if((c>a+b)||(b>a+c)||(a>b+c))
     {
    cout<<"Case #"<<curr<<": "<<"IMPOSSIBLE\n";
            curr++;
    }
        else{//r y b

            int maxi=max(a,max(b,c));
            if(maxi==c)
            {
                vector<char > temp1;
                vector<char > temp2;
                int smaxi=max(a,b);
                if(smaxi==a)
                {

                    while((a>0)&&(b>0))
                    {

                        temp1.push_back('R');
                        temp1.push_back('Y');
                        a--;
                        b--;
                    }

                    while(a>0)
                    {
                         temp1.push_back('R');
                        a--;
                    }


                }
                else
                {

                    while((a>0)&&(b>0))
                    {

                        temp1.push_back('Y');
                        temp1.push_back('R');
                        a--;
                        b--;
                    }

                    while(b>0)
                    {
                         temp1.push_back('Y');
                        b--;
                    }


                }
                int cu=temp1.size()-1;
                while((c>0)&&(cu>=0))
                {

                    temp2.push_back('B');
                    temp2.push_back(temp1[cu]);
                    cu--;
                    c--;
                }

                while(cu>=0)
                {

                    temp2.push_back(temp1[cu]);
                    cu--;
                }
                  cout<<"Case #"<<curr<<": ";
                for(int i=0;i<temp2.size();i++)
                    cout<<temp2[i];
                    cout<<"\n";
                    curr++;
            }


             else if(maxi==a)
            {
                vector<char > temp1;
                vector<char > temp2;
                int smaxi=max(c,b);
                if(smaxi==c)
                {

                    while((c>0)&&(b>0))
                    {

                        temp1.push_back('B');
                        temp1.push_back('Y');
                        c--;
                        b--;
                    }

                    while(c>0)
                    {
                        temp1.push_back('B');
                        c--;
                    }


                }
                //if(smaxi==b)
                else
                {

                    while((c>0)&&(b>0))
                    {

                        temp1.push_back('Y');
                        temp1.push_back('B');
                        c--;
                        b--;
                    }

                    while(b>0)
                    {
                         temp1.push_back('Y');
                         b--;

                    }


                }
                int cu=temp1.size()-1;
                while((a>0)&&(cu>=0))
                {

                    temp2.push_back('R');
                    temp2.push_back(temp1[cu]);
                    cu--;
                    a--;
                }

                while(cu>=0)
                {

                    temp2.push_back(temp1[cu]);
                    cu--;
                }
                cout<<"Case #"<<curr<<": ";
                for(int i=0;i<temp2.size();i++)
                    cout<<temp2[i];
                    cout<<"\n";
                    curr++;
            }

             else if(maxi==b)
            {
                vector<char > temp1;
                vector<char > temp2;
                int smaxi=max(a,c);
                if(smaxi==c)
                {

                    while((c>0)&&(a>0))
                    {

                        temp1.push_back('B');
                        temp1.push_back('R');
                        c--;
                        a--;
                    }

                    while(c>0)
                    {
                         temp1.push_back('B');
                        c--;
                    }


                }
                //if(smaxi==b)
                else
                {

                    while((c>0)&&(a>0))
                    {

                        temp1.push_back('R');
                        temp1.push_back('B');
                        a--;
                        c--;
                    }

                    while(a>0)
                    {
                         temp1.push_back('R');
                         a--;

                    }


                }
                int cu=temp1.size()-1;
                while((b>0)&&(cu>=0))
                {

                    temp2.push_back('Y');
                    temp2.push_back(temp1[cu]);
                    cu--;
                    b--;
                }

                while(cu>=0)
                {

                    temp2.push_back(temp1[cu]);
                    cu--;
                }
  cout<<"Case #"<<curr<<": ";
                for(int i=0;i<temp2.size();i++)
                    cout<<temp2[i];
                    cout<<"\n";
                    curr++;
            }
        }
    }
}
