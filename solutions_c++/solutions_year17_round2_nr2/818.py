#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=0;tc<t;tc++) {
        int n;
        cin>>n;
        int a1, a2, a3, b1, b2, b3;
        cin>>a1>>b1>>a2>>b2>>a3>>b3;
        bool lehet=true;
        if(a3<b1 || ( a3<b1+1 && b1!=0 && a1+a2>0 ) ) lehet=false;
        if(a1<b2 || ( a1<b2+1 && b2!=0 && a3+a2>0 ) ) lehet=false;
        if(a2<b3 || ( a2<b3+1 && b3!=0 && a1+a3>0 ) ) lehet=false;
        a1-=b2;
        a2-=b3;
        a3-=b1;
        if(a1>a2+a3) lehet=false;
        if(a2>a1+a3) lehet=false;
        if(a3>a2+a1) lehet=false;
        if(!lehet) {
            cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
        }
        else if(n==2*b1) {
            string sol;
            for(int i=0;i<b1;i++) {
                sol+="OB";
            }
            cout<<"Case #"<<tc+1<<": "<<sol<<endl;
        }
        else if(n==2*b2) {
            string sol;
            for(int i=0;i<b2;i++) {
                sol+="GR";
            }
            cout<<"Case #"<<tc+1<<": "<<sol<<endl;
        }
        else if(n==2*b3) {
            string sol;
            for(int i=0;i<b3;i++) {
                sol+="VY";
            }
            cout<<"Case #"<<tc+1<<": "<<sol<<endl;
        }
        else {
            stack<string> R;
            stack<string> B;
            stack<string> Y;
            for(int i=0;i<a1;i++) {
                string now;
                if(i==0) {
                    for(int j=0;j<b2;j++) {
                        now+="RG";
                    }
                }
                now+="R";
                R.push(now);
            }

            for(int i=0;i<a2;i++) {
                string now;
                if(i==0) {
                    for(int j=0;j<b3;j++) {
                        now+="YV";
                    }
                }
                now+="Y";
                Y.push(now);
            }

            for(int i=0;i<a3;i++) {
                string now;
                if(i==0) {
                    for(int j=0;j<b1;j++) {
                        now+="BO";
                    }
                }
                now+="B";
                B.push(now);
            }

            pair<int,stack<string> > x1=make_pair(a1,R);
            pair<int,stack<string> > x2=make_pair(a2,Y);
            pair<int,stack<string> > x3=make_pair(a3,B);
            if(x2.first<x3.first) {
                swap(x2,x3);
            }
            if(x1.first<x2.first) {
                swap(x1,x2);
            }

            vector<string> tab(x1.first);
            int it=0;
            for(int i=0;i<x2.first;i++) {

                tab[it%x1.first]+=x2.second.top();
                x2.second.pop();
                it++;
            }
            for(int i=0;i<x3.first;i++) {
                tab[it%x1.first]+=x3.second.top();
                x3.second.pop();
                it++;
            }
            string sol;
            for(int i=0;i<x1.first;i++) {
                sol+=x1.second.top();
                x1.second.pop();
                sol+=tab[i];
            }
            cout<<"Case #"<<tc+1<<": "<<sol<<endl;

        }
    }
    return 0;
}
