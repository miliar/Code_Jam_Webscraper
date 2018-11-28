#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <map>
#include <functional>

#define x first
#define y second


using namespace std;

int N;

bool cango(int a,int b){
    switch(a){
        case 0:
            return (b!=0 && b!=1 && b!=5);
        case 1:
            return (b!=0 && b!=1 && b!=2 && b!=3 && b!=5);
        case 2:
            return (b!=1 && b!=2 && b!=3);
        case 3:
            return (b!=1 && b!=2 && b!=3 && b!=4 && b!=5);
        case 4:
            return (b!=3 && b!=4 && b!=5);
        case 5:
            return (b!=0 && b!=1 && b!=3 && b!=4 && b!=5);

    }

}

vector<int> solve(vector<int> h, vector<int> current, int horses){
    vector<int> broken{-2};
    int r=h[0];int y=h[2];int b=h[4];

    int biggest=max(max(r,b),y);
    int smallest=min(min(r,b),y);
    int middle = r+y+b-biggest-smallest;

    if (biggest==1+smallest+middle && current.size()>0 && current[0]==0)r++;
    if (biggest==1+smallest+middle && current.size()>0 && current[0]==2)y++;
    if (biggest==1+smallest+middle && current.size()>0 && current[0]==4)b++;


    if (r>b+y){
        cout << r << " " << b << " " <<y<<endl;
            return broken;
    }
    if (b>r+y){
        cout << r << " " << b << " " <<y<<endl;
            return broken;
    }
    if (y>b+r){
        cout << r << " " << b << " " <<y<<endl;
            return broken;
    }

//    for (int i=0;i<current.size();i++)
//        cout << current[i] << " ";
//    cout << endl;
//cout << current.size() << endl;

    vector< pair<int,int> > toSort(h.size());
    for (int i=0;i<h.size();i++){
        toSort[i].x=h[i];
        toSort[i].y=i;
    }

    sort(toSort.begin(),toSort.end(),[](const pair< int,int >& a, const pair< int,int >& b){ return a.x > b.x; });

    for (int counter=0;counter<6;counter++){
        int i=toSort[counter].y;
        if (h[i]==0) continue;

        if (horses==1){ //last horse

            int last=current[current.size()-1];
            int first=current[0];
            if ( cango(last,i) && cango(first,i) ){
                current.push_back(i);

                return current;

            }


        }else if (horses==N){ //first horse

            current.push_back(i);
            h[i]--;
            vector<int> ret=solve(h,current,horses-1);
            if (ret[0]==-2){
                h[i]++;
                current.erase(current.end()-1);
                continue;
            }

            return ret;

        }else{
            int last=current[current.size()-1];
            if ( cango(last,i) ){
                current.push_back(i);
                h[i]--;
                vector<int> ret=solve(h,current,horses-1);
                if (ret[0]==-2){
                    h[i]++;
                    current.erase(current.end()-1);
                    continue;
                }

                return ret;

            }

        }


    }

    return broken;
}


int main(){
    std::map<int,char> m;

      m[0] = 'R';
      m[1] = 'O';
      m[2] = 'Y';
      m[3] = 'G';
      m[4] = 'B';
      m[5] = 'V';

    ofstream output("2.out");
    int t;
    cin >> t;
    for (int tt=0;tt<t;tt++){
        int R, O, Y, G, B, V;
        vector<int> h(6);
        cin >> N >> h[0] >> h[1] >> h[2]>> h[3]>> h[4]>> h[5];

        vector<int> emp;
        vector<int> ans = solve(h,emp,N);


        if (ans[0]==-2){
            output << "Case #" << tt+1 << ": " <<"IMPOSSIBLE"<< endl;
        }else{
            output << "Case #" << tt+1 << ": ";
            for (int i=0;i<ans.size();i++)
                output << m[ans[i]];
            output << endl;
        }

//        output << "Case #" << tt+1 << ": " <<"ans"<< endl;
//        cout << "Case #" << tt+1 << ": " <<"ans"<< endl;
    }


    return 0;
}
