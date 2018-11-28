#include<bits/stdc++.h>
using namespace std;
string place_pony(int r, int y, int b, char last){
    if(last=='R'){
        if(y>b&&y>0)
            return "Y"+place_pony(r,y-1,b,'Y');
        else if(b>0)
            return "B"+place_pony(r,y,b-1,'B');
        else return "";
    }
    else if(last=='Y'){
        if(r>b&&r>0)
            return "R"+place_pony(r-1,y,b,'R');
        else if(b>0)
            return "B"+place_pony(r,y,b-1,'B');
        else return "";
    }
    else{
        if(r>y&&r>0)
            return "R"+place_pony(r-1,y,b,'R');
        else if(y>0)
            return "Y"+place_pony(r,y-1,b,'Y');
        else return "";
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("small.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;
    cin>>t;
    i=1;
    while(i<=t){
        int n,r,o,y,g,b,v;
        string place="";
        cin>>n>>r>>o>>y>>g>>b>>v;
        if(r+y<b||r+b<y||b+y<r)
            place="IMPOSSIBLE";
        /*else{
            int f,s,t;
            char p[3];
            if(r==max(r,y,b)){
                f=r;
                p[0]='R';
                if(y==max(y,b)){
                    s=y;
                    p[1]='Y';
                    p[2]='B';
                }
                else {
                    s=b;
                    p[1]='B';
                    p[2]='Y';
                }
            }
            else if(y==max(r,y,b)){
                y=r;
                p[0]='Y';
                if(r==max(r,b)){
                    s=r;
                    p[1]='R';
                    p[2]='B';
                }
                else {
                    s=b;
                    p[1]='B';
                    p[2]='R';
                }
            else{
                f=b;
                p[0]='R';
                if(s==max(y,b)){
                    s=y;
                    p[1]='Y';
                    p[2]='B';
                }
                else {
                    s=b;
                    p[1]='B';
                    p[2]='Y';
                    }
                }
            }
        }*/
        else{
            place=place_pony(r,y,b,'R');
            if(place.back()==place.front())
                place=place_pony(r,y,b,'Y');
            if(place.back()==place.front())
                place=place_pony(r,y,b,'B');
        }
        cout<<"Case #"<<i<<": "<<place<<"\n";
        i++;
    }
    return 0;
}
