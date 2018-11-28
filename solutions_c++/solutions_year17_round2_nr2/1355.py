#include <iostream>
#include <list>
#include <iomanip>
#include <set>
#include <vector>
#include <cstring>
#include <algorithm>
#include <complex>
#include <map>
#include <queue>
#include <stack>
#include <functional>
#include <unordered_set>
#include <unordered_map>

using namespace std;
const int MAX = 5 * 10000;
const long long MOD = 1e9 + 7;
const double PI = 3.141592653589793238462643383279502884;
const double EPS = 1e-9;

double dist_stand(double x1, double y1, double x2, double y2){
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}
int dist_man(int x1, int y1, int x2, int y2){
    return (abs(x1 - x2) + abs(y1 - y2));
}





int main()
{
    int t;
    cin >> t;
    for(int ti = 0;ti<t;ti++){
        int n;
        cin >> n;
        int r,o,y,g,b,v;
        cin >> r >> o >> y >> g >> b >> v;
        string so="";
        string sg="";
        string sv="";

        if (b==o and n==b+o){
            string s = "";
            for (int i = 0;i<b;i++){
                s+="BO";
            }
            cout << "Case #"<< (ti+1) <<": " << s;
            continue;
        }
        if (r==g and n==r+g){
            string s = "";
            for (int i = 0;i<r;i++){
                s+="RG";
            }
            cout << "Case #"<< (ti+1) <<": " << s;
            continue;
        }
        if (y==v and n==y+v){
            string s = "";
            for (int i = 0;i<y;i++){
                s+="YV";
            }
            cout << "Case #"<< (ti+1) <<": " << s;
            continue;
        }

        bool can = true;


        if (b > o or o==0){
            if (o > 0){
                so = "B";
                b--;
                while (o > 0){
                    o--;b--;
                    so+="OB";
                }
                b++;
            }
        }
        else
            can = false;

        if (r > g or g==0){
            if (g > 0){
                sg = "R";
                r--;
                while (g > 0){
                    g--;r--;
                    sg+="GR";
                }
                r++;
            }
        }
        else
            can = false;

        if (y > v or v==0){
            if (v > 0){
                sv = "Y";
                y--;
                while (v > 0){
                    y--;v--;
                    sv+="VY";
                }
                y++;
            }
        }
        else
            can = false;


        if (y+r < b or y+b < r or b+r < y){
            can = false;
        }


        if(can){  // now only y,r,b and we can do it
            string s= "RYB";
            vector<int> num = {r,y,b};

            for(int i = 0;i<2;i++){
                for(int j = 0;j<2;j++){
                    if(num[j]<num[j+1]){
                        int z = num[j];  char c = s[j];
                        num[j] = num[j+1]; s[j] = s[j+1];
                        num[j+1] = z; s[j+1] = c;
                    }
                }
            }
            string res = "";


            while(num[0]+num[1]>=2){
                res = res +s[0]+s[1];
                num[0]--;num[1]--;

                if(num[1] < num[2]){
                    int z = num[1];  char c = s[1];
                    num[1] = num[2]; s[1] = s[2];
                    num[2] = z; s[2] = c;
                }
                if(num[0] < num[1]){
                    int z = num[0];  char c = s[0];
                    num[0] = num[1]; s[0] = s[1];
                    num[1] = z; s[1] = c;
                }
                if(num[1] < num[2]){
                    int z = num[1];  char c = s[1];
                    num[1] = num[2]; s[1] = s[2];
                    num[2] = z; s[2] = c;
                }
            }
            if(num[0]==1){
                char c = s[0];
                string newres="";
                int ind = 0;
                for(int i = 0;i<res.size() - 1;i++){
                    if(c!=res[i] and c!=res[i+1]){
                        ind = i;
                        break;
                    }
                }
                for(int i = 0;i<=ind;i++){
                    newres+=res[i];
                }
                newres=newres+c;
                for(int i = ind+1;i<res.size();i++){
                    newres+=res[i];
                }
                res = newres;
                num[0]--;
            }


            if (so.size()!=0){
                string newres = "";
                int ind = 0;
                for(int i = 0;i<res.size();i++){
                    if (res[i] =='B'){
                        ind = i;
                        break;
                    }
                }
                for(int i = 0;i<ind;i++){
                    newres+=res[i];
                }
                newres+=so;
                for(int i = ind+1;i<res.size();i++){
                    newres+=res[i];
                }
                res = newres;
            }
            if(sg.size()!=0){
                string newres = "";
                int ind = 0;
                for(int i = 0;i<res.size();i++){
                    if (res[i] =='R'){
                        ind = i;
                        break;
                    }
                }
                for(int i = 0;i<ind;i++){
                    newres+=res[i];
                }
                newres+=sg;
                for(int i = ind+1;i<res.size();i++){
                    newres+=res[i];
                }
                res = newres;
            }
            if(sv.size()!=0){
                string newres = "";
                int ind = 0;
                for(int i = 0;i<res.size();i++){
                    if (res[i] =='Y'){
                        ind = i;
                        break;
                    }
                }
                for(int i = 0;i<ind;i++){
                    newres+=res[i];
                }
                newres+=so;
                for(int i = ind+1;i<res.size();i++){
                    newres+=res[i];
                }
                res = newres;
            }

            cout << "Case #"<< (ti+1) <<": " << res;

        }
        else{
            cout << "Case #"<< (ti+1) <<": IMPOSSIBLE";
        }


        cout << endl;
    }

    return 0;
}