#include<iostream>
#include<algorithm>
#include<memory.h>
#include<stdio.h>
#include<string>
#include<vector>
#include<bitset>
#include<climits>
#include<fstream>
#include<conio.h>


using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;

struct s
{
    lli first;
    lli second;
};

/*display
for(lli m=0;m<v.size();m++)
{
    cout<<v[m].first<<' '<<v[m].second<<endl;

}
*/

int main()
{
    int t;
    lli n,k,y,z,p,left,right,num;
    ofstream a_out("c.txt");



    cin>>t;

    for(int tc=1;tc<=t;tc++)
    {

        cin>>n>>k;

        int a[500000]={0};

        fill_n(a,500000,0);

        vector< struct s > v;


        struct s s1;
        s1.first=n;
        s1.second=1;
        v.push_back(s1);

        for(lli i=1;i<=k-1;i++)
        {
            //cout<<"loop"<<endl;
            num = v[0].first;
            //cout<<num<<endl;
            if(num%2 != 0)
            {
                left = num/2;
                right = left;

                //cout<<left<<' '<<right<<endl;
                if(v[v.size()-1].first > right)
                {
                    //cout<<"if"<<endl;
                    s1.first=right;
                    s1.second=2;
                    v.push_back(s1);
                }
                else
                {
                    //cout<<"else"<<endl;
                    for(lli j=1;j<v.size();j++)
                    {
                        if(v[j].first == right)
                        {
                            v[j].second+=2;
                        }
                    }
                }
            }
            else
            {
                right = num/2;
                left = right -1;
                //cout<<"else "<<right<<' '<<left<<endl;
                if(v[v.size()-1].first > right)
                {
                    s1.first=right;
                    s1.second=1;
                    v.push_back(s1);
                }
                else
                {
                    for(lli j=1;j<v.size();j++)
                    {
                        if(v[j].first == right)
                        {
                            v[j].second++;
                        }
                    }
                }

                if(v[v.size()-1].first > left)
                {
                    s1.first=left;
                    s1.second=1;
                    v.push_back(s1);
                }
                else
                {
                    for(lli j=1;j<v.size();j++)
                    {
                        if(v[j].first == left)
                        {
                            v[j].second++;
                        }
                    }
                }
            }


            /*for(lli m=0;m<v.size();m++)
            {
                cout<<v[m].first<<' '<<v[m].second<<endl;

            }*/

            v[0].second--;
            if(v[0].second == 0)
                v.erase(v.begin());

            /*cout<<"erased"<<endl;
            for(lli m=0;m<v.size();m++)
            {
                cout<<v[m].first<<' '<<v[m].second<<endl;

            }*/

            //getch();

        }

        if((v[0].first) %2 != 0 )
        {
            y = (v[0].first)/2;

            z = y;
        }
        else
        {
            y = (v[0].first)/2;

            z=y-1;
        }

        cout<<"Case #"<<tc<<": "<<y<<" "<<z<<endl;
        a_out<<"Case #"<<tc<<": "<<y<<" "<<z<<endl;
    }

    return 0;
}
