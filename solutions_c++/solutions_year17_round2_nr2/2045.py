#include<bits/stdc++.h>
using namespace std;

vector<string>vc;

bool ok(int r,int y,int b,string fs)
{
    string pre=fs;
    string sc;
    int ck=1;
    while(r>0 || y>0 || b>0)
    {
        if(r>=y && r>=b)
        {
            if(pre!="R")
            {
                sc="R";
                vc.push_back("R");
                r--;
                pre="R";
            }
            else
            {
                if(y>=b && pre!="Y" && y>0)
                {

                    sc="Y";
                    vc.push_back("Y");
                    y--;
                    pre="Y";
                }
                else if(pre!="B" && b>0)
                {

                    sc="B";
                    vc.push_back("B");
                    b--;
                    pre="B";
                }
                else return 0;
            }
        }
        else if(y>=r && y>=b)
        {
            if(pre!="Y")
            {

                sc="Y";
                vc.push_back("Y");
                y--;
                pre="Y";
            }
            else
            {
                if(r>=b && pre!="R" && r>0)
                {

                    sc="R";
                    vc.push_back("R");
                    r--;
                    pre="R";
                }
                else if(pre!="B" && b>0)
                {

                    sc="B";
                    vc.push_back("B");
                    b--;
                    pre="B";
                }
                else return 0;
            }
        }
        else if(b>=r && b>=y)
        {
            if(pre!="B")
            {

                sc="B";
                vc.push_back("B");
                b--;
                pre="B";
            }
            else
            {
                if(y>=r && pre!="Y" && y>0)
                {

                    sc="Y";
                    vc.push_back("Y");
                    y--;
                    pre="Y";
                }
                else if(pre!="R" && r>0)
                {

                    sc="R";
                    vc.push_back("R");
                    r--;
                    pre="R";
                }
                else return 0;
            }
        }
    }
    return fs!=sc;

}


int main()
{
    freopen("B-small-attempt8.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,i,j;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {

        int r,y,b,o,g,v,n;
        scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",ca);

        vc.clear();
        if(r>0)
        {
            vc.push_back("R");
            if(ok(r-1,y,b,"R"))
            {
                for(int i=0; i<vc.size(); i++) cout <<vc[i];
                cout <<endl;
                continue;
            }
        }
        vc.clear();
        if(b>0)
        {
            vc.push_back("B");
            if(ok(r,y,b-1,"B"))
            {
                for(int i=0; i<vc.size(); i++) cout <<vc[i];
                cout <<endl;
                continue;
            }
        }
        vc.clear();
        if(y>0)
        {
            vc.push_back("Y");
            if(ok(r,y-1,b,"Y"))
            {
                for(int i=0; i<vc.size(); i++) cout <<vc[i];
                cout <<endl;
                continue;
            }
        }

        cout <<"IMPOSSIBLE"<<endl;

        vc.clear();

    }
}

