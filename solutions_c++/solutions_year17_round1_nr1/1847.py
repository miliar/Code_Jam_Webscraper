#include <iostream>
#include <cstring>
#include <cstdio>
#include <climits>
#define lli long long int
using namespace std;
void prin();
char num[25][25];
lli t,j,r,c;
char ch;

int main()
{
    freopen("in2.in","r",stdin);
    freopen("ans2.txt","w",stdout);
    cin>>t;
    for(int i = 1 ; i <=t ; ++i)
    {
        cin>>r>>c;
        for(lli j = 0 ; j < r ; ++j)
        {
            for(lli k = 0 ; k < c ; ++k)
            {
                cin>>num[j][k];
            }
        }
        lli temp;
        for(lli j = 0 ; j < r ; ++j)
        {
            for(lli k = 0 ; k < c ; ++k)
            {
                temp = k;
                ch = num[j][k];
                if(ch != '?')
                {
                    for(lli p = k+1 ; p < c ; ++p)
                    {
                        if(num[j][p] == '?')
                        {
                            num[j][p] = ch;
                            temp = temp + 1;
                        }
                        else{break;}

                    }
                }
                if(temp!= k){k = temp-1;}
            }
        }

        for(lli j = 0 ; j < r ; ++j)
        {
            ch=';';
            for(lli k = 0 ; k < c ; ++k)
            {
                if(num[j][k] == '?')
                {
                    for(lli p = k+1 ; p < c ; ++p)
                    {
                        if(num[j][p]!= '?'){ch = num[j][p];break;}
                    }
                }
                if(ch != ';')
                {
                    num[j][k] = ch;
                    for(lli p= k+1 ; p < c ; ++p)
                    {
                        if(num[j][p] == '?'){num[j][p] = ch;}
                        else{break;}
                    }
                    break;
                }
            }
        }


        for(lli k = 0 ; k < c ; ++k)
        {
            ch = ';';
            for(lli j = 0 ; j < r; ++j)
            {
                if(num[j][k] == '?')
                {
                    for(lli p = j+1 ; p < r ; ++p)
                    {
                        if(num[p][k] !='?'){ch = num[p][k];break;}
                    }
                }
                if(ch!=';')
                {
                    num[j][k] = ch;
                    for(lli p = j+1 ; p < r ; ++p)
                    {
                        if(num[p][k] == '?'){num[p][k] = ch;}else{j = p-1;break;}
                    }
                    ch = ';';

                }
            }
        }

        for(lli k = 0 ; k < c ; ++k)
        {
            for(lli j = 0 ; j < r ; ++j)
            {
                if(num[j][k]!= '?'){ch = num[j][k];}
                else{num[j][k] = ch;}
            }
        }
        cout<<"Case #"<<i<<":"<<endl;
        prin();
    }
    return 0;

}
void prin()
{
    for(lli o = 0 ; o < r ; ++o)
    {
        for(lli h = 0 ; h < c ; ++h)
        {
            cout<<num[o][h];
        }
        cout<<"\n";
    }
}
