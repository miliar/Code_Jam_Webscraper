#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main()
{


    int t,n,r,o,y,g,b,v;
    cin >> t;
    for(int q = 1;q<=t ;q++){
        cin >> n>>r>>o>>y>>g>>b>>v;

        if(r>y+b || y>r+b || b>r+y) cout << "Case #"<<q<<": "<<"IMPOSSIBLE" << endl;
        else{
        bool chk =false;
            string s = "";
            priority_queue<pair<int,string>> pq;
            if(b>0)pq.push(make_pair(b,"B"));
            if(r>0)pq.push(make_pair(r,"R"));
            if(y>0)pq.push(make_pair(y,"Y"));
            pair<int,string> p1;
            pair<int,string> p2;
            while(!pq.empty()){
                    chk = false;
                p1 = pq.top();
                pq.pop();
                if(!pq.empty()){
                    p2 = pq.top();
            chk = true;
                pq.pop();}
                s += p1.second;
                if(chk)s += p2.second;

                p1.first -=1;
                p2.first -=1;
                if(p1.first >0) pq.push(p1);
                if(p2.first>0) pq.push(p2);
                //cout << s << endl;
            }
            //cout << s << endl;
            if(s[0] == s[s.size()-1]){
                string c = s.substr(0,1);
                if(c == "B"){
                    int w = s.find("RY");
                    if(w>=0){
                        s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }else{
                    w = s.find("YR");
                    s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }
                }else if(c == "R"){
                    int w = s.find("BY");
                    if(w>=0){
                        s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }else{
                    w = s.find("YB");
                    s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }
                }else if(c == "Y"){
                    int w = s.find("RB");
                    if(w>=0){
                        s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }else{
                    w = s.find("BR");
                    s.insert(w+1,c);
                        s.erase(s.size()-1,1);
                    }
                }
            }


            cout << "Case #"<<q<<": "<<s << endl;


        }
    }
    return 0;
}
