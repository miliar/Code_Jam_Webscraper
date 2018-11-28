#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

// std::numeric_limits<T>::max() 

void main2(){
	int AC, AJ;
	cin>> AC >> AJ;
    vector<pair<int,int>> C(AC);
    for(int i=0;i<AC;i++){
        cin >> C[i].first >> C[i].second;
    }
    vector<pair<int,int>> J(AJ);
    for(int i=0;i<AJ;i++){
        cin >> J[i].first >> J[i].second;
    }
    sort(C.begin(),C.end());
    sort(J.begin(),J.end());

    int result = 0;

    int fixed_J_care=0;
    int fixed_C_care=0;
    int flexible_time=0;
    vector<int> default_J_care;
    vector<int> default_C_care;
    vector<int> default_J_care_edge;
    vector<int> default_C_care_edge;
    int i=0;
    int j=0;

    int last_person=-1; //0=C care, 1=J care
    int last_care_end=0;

    if(AC==0) last_person=0;
    if(AJ==0) last_person=1;
    if(AC>0 && AJ>0){
        if(J[j].first < C[i].first){ // J duty comes first
            last_person=0;
        }else{
            last_person=1;
        }
    }
    if(last_person==0){
        default_C_care_edge.push_back(J[j].first - last_care_end);
        fixed_C_care += J[j].second-J[j].first;
        last_care_end=J[j].second;
        j++;
    }else{
        default_J_care_edge.push_back(C[i].first - last_care_end);
        fixed_J_care += C[i].second-C[i].first;
        last_care_end=C[i].second;
        i++;
    }

    while(i<AC || j<AJ){
        if(i>=AC || j<AJ && J[j].first < C[i].first){ // J duty comes first
            if(last_person==1){ // has to switch
                flexible_time += J[j].first - last_care_end;
                result++;
            }else{
                default_C_care.push_back(J[j].first - last_care_end);
            }
            fixed_C_care += J[j].second-J[j].first;
            last_person=0;
            last_care_end=J[j].second;
            j++;
            continue;
        }

        if(j>=AJ || i<AC && C[i].first < J[j].first ){ // C duty comes first
            if(last_person==0){ // has to switch
                flexible_time += C[i].first - last_care_end;
                result++;
            }else{
                default_J_care.push_back(C[i].first - last_care_end);
            }
            fixed_J_care += C[i].second-C[i].first;
            last_person=1;
            last_care_end=C[i].second;
            i++;
            continue;
        }
    }
    if(last_person==0){
        default_C_care_edge.push_back(1440-last_care_end);
    }else{
        default_J_care_edge.push_back(1440-last_care_end);
    }
    
    if(default_J_care_edge.size()==2){
        default_J_care.push_back(default_J_care_edge[0]+default_J_care_edge[1]);
        default_J_care_edge.clear();
    }
    if(default_C_care_edge.size()==2){
        default_C_care.push_back(default_C_care_edge[0]+default_C_care_edge[1]);
        default_C_care_edge.clear();
    }
    if(default_C_care_edge.size()==1){
        flexible_time+=(default_C_care_edge[0]+default_J_care_edge[0]);
        result++;
        default_C_care_edge.clear();
        default_J_care_edge.clear();
    }

    cerr<< fixed_J_care<<endl;
    cerr<< fixed_C_care<<endl;
    cerr<< flexible_time<<endl;
    sort(default_J_care.begin(),default_J_care.end(),greater<int>());
    sort(default_C_care.begin(),default_C_care.end(),greater<int>());
    sort(default_J_care_edge.begin(),default_J_care_edge.end(),greater<int>());
    sort(default_C_care_edge.begin(),default_C_care_edge.end(),greater<int>());
    for(auto jc:default_J_care)
        cerr << jc << ',';
    cerr<<endl;
    for(auto jc:default_J_care_edge)
        cerr << jc << ',';
    cerr<<endl;
    for(auto cc:default_C_care)
        cerr << cc << ',';
    cerr<<endl;
    for(auto cc:default_C_care_edge)
        cerr << cc << ',';
    cerr<<endl;
    cerr<< result<<endl;
    

    int total_J_care = fixed_J_care;
    for(auto jc:default_J_care) total_J_care+=jc;
    for(auto jc:default_J_care_edge) total_J_care+=jc;
    if(total_J_care <= 720 && total_J_care+flexible_time >= 720){
        cout << result;
        return;
    }
    int min_addition = std::numeric_limits<int>::max() ;
    if(total_J_care + flexible_time < 720){ // change some C care to J
        for(int i=0;i<=default_C_care_edge.size();i++){
            int tmp_addition=0;
            int additional_flexible_time=0;
            for(int j=0;j<i;j++){
                additional_flexible_time+=default_C_care_edge[j];
                tmp_addition++;
            }
            int j=0;
            while(j<default_C_care.size() && total_J_care+flexible_time+additional_flexible_time < 720){
                additional_flexible_time+=default_C_care[j];
                tmp_addition+=2;
                j++;
            }
            if(total_J_care+flexible_time+additional_flexible_time >= 720)
                min_addition=min(min_addition,tmp_addition);
        }
        result+=min_addition;
    }
    if(total_J_care > 720){
        // change J_care to C;
        for(int i=0;i<=default_J_care_edge.size();i++){
            int tmp_addition=0;
            int additional_flexible_time=0;
            for(int j=0;j<i;j++){
                additional_flexible_time+=default_J_care_edge[j];
                tmp_addition++;
            }
            int j=0;
            while(j<default_J_care.size() && total_J_care-additional_flexible_time > 720){
                additional_flexible_time+=default_J_care[j];
                tmp_addition+=2;
                j++;
            }
            if(total_J_care-additional_flexible_time <= 720)
                min_addition=min(min_addition,tmp_addition);
        }
        result+=min_addition;
    }
    


    cout << result;
}

int main(){
    string core;
    //core="C-small-practice";
    core="B-small-attempt1";
    freopen ( (core+".in").c_str(), "r", stdin );
    freopen ( (core+".out").c_str(), "w", stdout );
	int T;
	cin>>T;

	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		cerr<<"Case #"<<t+1<<": "<<endl;;
		main2();
		cout<<endl;
	}
    
    fclose (stdin);
    fclose (stdout);
}
