#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int findPos(vector<char> stalls){
    int pos = -1;
    int mini = -1;
    int maxi = -1;
    int ls,rs;
    vector<int> maxl;
    vector<int> minl;
    vector<int> posl;
    for(int i = 1;i<stalls.size()-1;i++){
        if (stalls[i] == 'o') continue;
        ls = i-1;
        rs = i+1;
        while(1){
            if (stalls[ls] == '.')
                ls--;
            else
                break;
        }
        ls = i - ls - 1;
        while(1){
            if (stalls[rs] == '.')
                rs++;
            else
                break;
        }
        rs = rs - i - 1;
        int tempmini = min(ls,rs);
        int tempmaxi = max(ls,rs);
        if(tempmini > mini){
            maxl.clear();
            minl.clear();
            posl.clear();
            mini = tempmini;
            maxi = tempmaxi;
            pos = i;
            maxl.push_back(maxi);
            minl.push_back(mini);
            posl.push_back(pos);
        }else if(tempmini == mini){
            mini = tempmini;
            maxi = tempmaxi;
            pos = i;
            maxl.push_back(maxi);
            minl.push_back(mini);
            posl.push_back(pos);

        }

    }
    if(posl.size()>1){
        vector<int> second_max;
        vector<int> second_pos;
        maxi = -1;
        int index = -1;
        for (int i = 0;i < maxl.size();i++){
            if(maxl[i] > maxi){
                second_max.clear();
                second_pos.clear();
                maxi = maxl[i];
                index = i;
                second_max.push_back(maxi);
                second_pos.push_back(index);
            }else if(maxl[i] == mini){
                maxi = maxl[i];
                index = i;
                second_max.push_back(maxi);
                second_pos.push_back(index);
            }
        }
        return posl[second_pos[0]];
    }
    return posl[0];

}


void getLast(vector<char> stalls, int n, int k, int & mini, int & maxi){
    int pos;
    while(k--){
        pos = findPos(stalls);
        //cout<<pos<<endl;
        stalls[pos] = 'o';
    }
    int ls,rs;
    ls = pos -1;
    rs = pos + 1;
    while(1){
        if(stalls[ls] == '.')
            ls--;
        else
            break;
    }
    while(1){
        if(stalls[rs] == '.')
            rs++;
        else
            break;
    }
    ls = pos - ls -1;
    rs = rs - pos -1;
    mini = min(ls,rs);
    maxi = max(ls,rs);
}

int main(){
    int t;
    cin>>t;
    int n;
    int k;
    int i = 1;
    while(t--){
        cin>> n >> k;
        vector<char> stalls(n+2,'.');
        stalls[0] = 'o';
        stalls[n+1] = 'o';
        int min;
        int max;
        getLast(stalls,n,k,min,max);
        cout<<"Case #"<<i++<<": "<<max<<' '<<min<<endl;
        /*for(int j = 0;j<stalls.size();j++)
            cout<<stalls[j];
        cout<<endl;*/
    }
    return 0;
}
