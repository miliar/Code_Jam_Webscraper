/* 
 * Prob:  
 * Author: sameerpandit
 *
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <climits>

using namespace std;
#define ull long long

int main() {
    bool debug=false;
    int T;
    cin>>T;
    int t = T;    
    while (T--) {
        ull n,k;
        cin>>n>>k;
        vector<pair<ull,ull> > left(n);
        vector<pair<ull,ull> > right(n);
        vector<ull> occupied(n);
        cout << "Case #" << t - T << ": ";
        if(debug)
            cout<<endl;
        //ans goes her
        for(int i=0;i<n;i++){
            left[i]=make_pair(i,0);
            right[i]=make_pair(n-i-1,n-1);
        }
        ull minVal,maxVal;
        for(ull i=0;i<k;i++){
            set<ull> feasibleFirstJ;
            set<ull>::iterator it;
            set<ull> feasibleSecondJ;
            ull maxFirstVal=0,maxSecondVal=-1;
            ull choosen;
            if(debug){
                for(ull j=0;j<n;j++){
                    if(!occupied[j])
                        cout<<left[j].first<<" ";
                }
                cout<<endl;
                for(ull j=0;j<n;j++){
                    if(!occupied[j])
                        cout<<right[j].first<<" ";
                }
                cout<<endl;
            }
            for(ull j=0;j<n;j++){
                if(!occupied[j]){
                    if(maxFirstVal<min(left[j].first,right[j].first)){
                        maxFirstVal=min(left[j].first,right[j].first);
                        feasibleFirstJ.clear();
                        feasibleFirstJ.insert(j);
                    }else if(maxFirstVal==min(left[j].first,right[j].first)){
                        feasibleFirstJ.insert(j);
                    }
                }
            }
            if(debug){
                for(it=feasibleFirstJ.begin();it!=feasibleFirstJ.end();it++){
                    cout<<*it<<" ";
                }
                cout<<endl;
            }
//            cout<<feasibleFirstJ.size()<<endl;
            if(feasibleFirstJ.size()==1)
                choosen=(*feasibleFirstJ.begin());
            else{
                for(it=feasibleFirstJ.begin();it!=feasibleFirstJ.end();it++){
                    if(maxSecondVal<max(left[*it].first,right[*it].first)){
                        maxSecondVal=max(left[*it].first,right[*it].first);
                        choosen=*it;
                    }
                }
            }
            minVal=min(left[choosen].first,right[choosen].first);
            maxVal=max(left[choosen].first,right[choosen].first);
            occupied[choosen]=1;
            for(ull j=0;j<n;j++){
                if(debug)
                    if(occupied[j])
                        cout<<"0";
                    else
                        cout<<".";
                if(!occupied[j]){
                    if(j>choosen && left[j].second<=choosen){
                        left[j]=make_pair((left[j].first-choosen+left[j].second-1),choosen+1);                    
                    }else if(j<choosen && right[j].second>=choosen){
                        right[j]=make_pair((right[j].first-right[j].second+choosen-1),choosen-1);
                    }
                }                
            }
            if(debug)
                cout<<endl;
        }
        cout<<maxVal<<" "<<minVal;
        cout << endl;
    }
    return 0;
}
