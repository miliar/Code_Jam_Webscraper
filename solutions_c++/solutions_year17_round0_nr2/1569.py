#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <climits>
#include <queue>
#include <iomanip>
#include <cstdio>
#define lli long long int
#include<fstream>
using namespace std;

int main()
{
    ifstream cin("B-large.in");
	ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        string st;
       cin>>st;

        int n=st.length(),p=-1;
        for(int i=1;i<n;i++){
            if(st[i]<st[i-1])
            {
                p=i-1;
                break;
            }
        }
        if(p!=-1){
                int i=p;
        char c=st[p],cp=(char)(st[p]-1);
            while(i>=0&&st[i]==c)
                    i--;
            i++;
            st[i]=cp;
            i++;
            for(;i<n;i++)
                st[i]='9';
        }


        cout<<"Case #"<<tt<<": ";
        if(st[0]!='0')
            cout<<st[0];
        cout<<st.substr(1)<<endl;

    }
}


