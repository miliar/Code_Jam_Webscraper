//Aditya Agrawal
// DTU


#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <list>
#include <utility>
#include <iterator>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <bitset>
#include <complex>
//#include <unordered_set>
//#include <unordered_map>


#define mod 1000000007
#define ima 1000000004
#define imi -1000000004
#define llma 1000000000000000004
#define llmi -1000000000000000004
#define lp(i,n) for(i=0;i<n;i++)
#define li(i,n) for(i=n-1;i>=0;i--)
#define tree vector<list<int > >
#define ll long long int
#define ld long double
#define f first
#define s second
#define pa pair<ll,ll>
#define pad pair<double ,double>
#define pai pair<int,int>
#define mp make_pair
#define nn 1005
#define pi 3.1415926535898
#define inf 1e35
#define diff 1e-7
#define md 359999
#define it ::iterator
#define pb push_back
#define sync ios::sync_with_stdio(false);cout.tie(0);cin.tie(0);

using namespace std;

typedef complex<double> base;

struct numb
{
    int orange,red,violet,blue,green,yellow;
};

char sol[nn];
int n;




int main()
{
    sync
    int t;
    cin>>t;
    int j=0;
    numb cur;
    int i;
    int flag=0;
    while(t--)
    {
        j++;
        cin>>n;
        sol[n]='\0';
        cout<<"Case #"<<j<<": ";
        cin>>cur.red>>cur.orange>>cur.yellow>>cur.green>>cur.blue>>cur.violet;
        if(cur.red+cur.orange+cur.violet>n/2)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else if(cur.blue+cur.green+cur.violet>n/2)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else if(cur.yellow+cur.orange+cur.green>n/2)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            if(cur.red>0)
            {
                sol[0]='R';
                cur.red--;
            }
            else if(cur.blue>0)
            {
                sol[0]='B';
                cur.blue--;
            }
            else if(cur.green>0)
            {
                sol[0]='G';
                cur.green--;
            }
            else if(cur.yellow>0)
            {
                sol[0]='Y';
                cur.yellow--;
            }
            else if(cur.violet>0)
            {
                sol[0]='V';
                cur.violet--;
            }
            else if(cur.orange>0)
            {
                sol[0]='O';
                cur.orange--;
            }
            i=1;
            flag=0;
            while(i<n-1)
            {
                if(sol[i-1]=='R' || sol[i-1]=='B' || sol[i-1]=='Y')
                {
                    if(sol[i-1]=='R')
                    {
                        if(cur.green>0)
                        {
                            cur.green--;
                            sol[i]='G';
                        }
                        else if(cur.blue>cur.yellow && cur.blue>0)
                        {
                            cur.blue--;
                            sol[i]='B';
                        }
                        else if(cur.yellow>0)
                        {
                            cur.yellow--;
                            sol[i]='Y';
                        }
                        else
                        {
                            flag=1;
                            break;
                        }
                    }
                    else if(sol[i-1]=='Y')
                    {
                        if(cur.violet>0)
                        {
                            cur.violet--;
                            sol[i]='V';
                        }
                        else if(cur.blue>cur.red && cur.blue>0)
                        {
                            cur.blue--;
                            sol[i]='B';
                        }
                        else if(cur.red>0)
                        {
                            cur.red--;
                            sol[i]='R';
                        }
                        else
                        {
                            flag=1;
                            break;
                        }
                    }
                    else
                    {
                        if(cur.orange>0)
                        {
                            cur.orange--;
                            sol[i]='O';
                        }
                        else if(cur.red>cur.yellow && cur.red>0)
                        {
                            cur.red--;
                            sol[i]='R';
                        }
                        else if(cur.yellow>0)
                        {
                            cur.yellow--;
                            sol[i]='Y';
                        }
                        else
                        {
                            flag=1;
                            break;
                        }
                    }
                    
                }
                else if(sol[i-1]=='O')
                {
                    if(cur.blue<=0)
                    {
                        flag=1;
                        break;
                    }
                    sol[i]='B';
                    cur.blue--;
                }
                else if(sol[i-1]=='G')
                {
                    if(cur.red<=0)
                    {
                        flag=1;
                        break;
                    }
                    sol[i]='R';
                    cur.red--;
                }
                else
                {
                    if(cur.yellow<=0)
                    {
                        flag=1;
                        break;
                    }
                    sol[i]='Y';
                    cur.yellow--;
                }
                i++;
            }
            
            if(!flag)
            {
                if(cur.yellow>0)
                {
                    if(sol[0]=='O' || sol[0]=='G' || sol[0]=='Y' || sol[i-1]=='O' || sol[i-1]=='G' || sol[i-1]=='Y')
                    {
                        flag=1;
                    }
                    else
                        sol[i]='Y';
                }
                else if(cur.green>0)
                {
                    if( sol[i-1]=='R' &&  sol[0]=='R')
                    {
                        sol[i]='G';
                    }
                    else
                        flag=1;
                }
                else if(cur.red>0)
                {
                    if(sol[0]=='R' || sol[0]=='O' || sol[0]=='V' || sol[i-1]=='O' || sol[i-1]=='R' || sol[i-1]=='V')
                    {
                        flag=1;
                    }
                    else
                        sol[i]='R';
                    //return true;
                }
                else if(cur.blue>0)
                {
                    if(sol[0]=='B' || sol[0]=='G' || sol[0]=='V' || sol[i-1]=='B' || sol[i-1]=='G' || sol[i-1]=='V')
                    {
                        flag=1;
                    }
                    else
                        sol[i]='B';
                    // return true;
                }
                else if(cur.orange>0)
                {
                    if( sol[i-1]=='B' &&  sol[0]=='B')
                    {
                        sol[i]='O';
                    }
                    else
                        flag=1;
                }
                else if(cur.violet>0)
                {
                    if( sol[i-1]=='Y' &&  sol[0]=='Y')
                    {
                        sol[i]='V';
                    }
                    else
                        flag=1;
                }
            }
            
            if(flag)
                cout<<"IMPOSSIBLE\n";
            else
                cout<<sol<<endl;
        }
    }
    
}
