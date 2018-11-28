#include<iostream>
#include<fstream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;

string str1,str2,str3;

string solv1( int R,int O,int Y,int G,int B,int V)
{
    char ch[3]={'R','B','Y'};


        if(B>=Y&&B>=R)
        {
            ch[0]='B';
            ch[1]='R';
            swap(R,B);
            swap(str1,str2);
        } else if( Y>=B&&Y>=R)
        {
            ch[0]='Y';
            ch[2]='R';
            swap(str1,str3);
            swap(R,Y);
        }

        int fR=1,fB=1,fY=1;
        string ans;
        if(R>B+Y)
        {
            ans="IMPOSSIBLE";
        }
        else
        {
            while(R<B+Y)
            {
                if(fR)
                {
                    ans+=str1;
                    fR=0;
                }else ans+=ch[0];

                if(fB)
                {
                    ans+=str2;
                    fB=0;
                }else ans+=ch[1];

                if(fY)
                {
                    ans+=str3;
                    fY=0;
                }else ans+=ch[2];


                R--;
                B--;
                Y--;
            }
            while(B--)
            {
                if(fR)
                {
                    ans+=str1;
                    fR=0;
                }else ans+=ch[0];

                if(fB)
                {
                    ans+=str2;
                    fB=0;
                }else ans+=ch[1];

            }
            while(Y--)
            {
                if(fR)
                {
                    ans+=str1;
                    fR=0;
                }else ans+=ch[0];

                if(fY)
                {
                    ans+=str3;
                    fY=0;
                }else ans+=ch[2];

            }
        }
    return ans;
}

int main()
{
    ifstream ifile("B-large.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        int n,R,O,Y,G,B,V;
        cin>>n>>R>>O>>Y>>G>>B>>V;

        string ans;
        if(R+O+Y+G+B+V==R+G)
        {
           // cout<<"%%";
            if(R==G)
            {
                while(R--)
                {
                    ans+="RG";
                }
            }
            else
            {
                ans="IMPOSSIBLE";
            }
        }
        else if(R+O+Y+G+B+V==B+O)
        {
               // cout<<"^^";
            if(B==O)
            {
                while(B--)
                {
                    ans+="BO";
                }
            }
            else
            {
                ans="IMPOSSIBLE";
            }
        }
        else if(R+O+Y+G+B+V==Y+V)
        {
           // cout<<"&&";
            if(Y==V)
            {
                while(Y--)
                {
                    ans+="YV";
                }
            }
            else
            {
                ans="IMPOSSIBLE";
            }
        }
        else if(G>R||O>B||V>Y||(G&&R==G)||(Y&&Y==V)||(B&&B==O))
        {
            //cout<<"**";
            ans="IMPOSSIBLE";
        }
        else
        {
            //cout<<"here";
            str1="R";
            while(G--)
            {
                R--;
                str1+="GR";
            }

            str2="B";
            while(O--)
            {
                B--;
                str2+="OB";
            }

            str3="Y";
            while(V--)
            {
                Y--;
                str3+="VY";
            }
           // cout<<R<<" "<<Y<<" "<<B<<" "<<str1<<" "<<str2<<" "<<str3<<"\n";
            ans=solv1(R,O,Y,G,B,V);
        }


        cout<<"Case #"<<fff<<": "<<ans<<"\n";
    }
    return 0;
}
