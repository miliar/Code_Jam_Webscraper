#include<bits/stdc++.h>
using namespace std;


struct stall{
    long long num;
    long long index;
};

long long min(long long a, long long b){
    return a<b?a:b;
}

long long max(long long a, long long b){
    return a>b?a:b;
}

vector<long long> bath;
long long finalls, finalrs;

void findpos(long long n){
        vector<long long> ls, rs;
        for(long long i=1; i<=n; i++){
            if(bath[i]==0){
                long long count = 0;
                for(long long j=i+1; j<=n+1; j++){
                    count++;
                    if(bath[j]==1){
                        break;
                    }
                }
                ls.push_back(count);
            }
        }
        for(long long i=1; i<=n; i++){
            if(bath[i]==0){
                long long count = 0;
                for(long long j=i-1; j>=0; j--){
                    count++;
                    if(bath[j]==1){
                        break;
                    }
                }
                rs.push_back(count);
            }
        }
        //for(long long i=0; i<ls.size(); i++){
        //    cout << ls[i] << " " << rs[i] << endl;
        //}
        vector<long long> pos;
        for(long long i=0; i<ls.size(); i++){
            long long temp = min(ls[i], rs[i]);
            pos.push_back(temp);
        }
        long long maxim = -1, index;
        bool flag = false;
        for(long long i=0; i<pos.size(); i++){
            if(maxim<pos[i]){
                maxim = pos[i];
                index = i;
            }
            else if(maxim==pos[i]){
                flag = true;
            }
        }
        long long tempindex;
        if(flag){
            vector<stall> pos2, ls2, rs2;

            for(long long i=0; i<pos.size(); i++){
                if(pos[i]==maxim){
                    stall temp;
                    temp.num = ls[i];
                    temp.index = i;
                    ls2.push_back(temp);
                    temp.num = rs[i];
                    rs2.push_back(temp);
                }
            }
            maxim = -1;
            for(long long i=0; i<ls2.size(); i++){
                //cout << ls2[i] << " " << rs2[i] << endl;
                long long temp = max(ls2[i].num, rs2[i].num);
                stall temp2;
                temp2.num = temp;
                temp2.index = ls2[i].index;
                pos2.push_back(temp2);
            }
            for(long long i=0; i<pos2.size(); i++){
                if(maxim<pos2[i].num){
                    maxim = pos2[i].num;
                    tempindex = pos2[i].index;
                    index = tempindex;
                }
            }
        }

        long long zero = 0;
        long long i;
        for(i=0; i<bath.size(); i++){
            if(bath[i]==0){
                zero++;
            }
            if(zero==(index+1)){
                bath[i]=1;
                break;
            }
        }
        long long count = 0;
        for(long long j=i+1; j<=n+1; j++){
            count++;
            if(bath[j]==1){
                break;
            }
        }
        finalls = count;

        count = 0;
        for(long long j=i-1; j>=0; j--){
            count++;
            if(bath[j]==1){
                break;
            }
        }
        finalrs = count;
        //for(long long j=0; j<bath.size(); j++){
        //cout << bath[j] << " ";
        //}
        //cout << endl;
}

int main(){
    freopen("inputlarge.in","r",stdin);
    freopen("outputlarge.out","w",stdout);
    long long t;
    cin >> t;
    long long tc = 0;
    while(t--){
        finalls = 0;
        finalrs = 0;
        bath.clear();
        tc++;
        long long n, k;
        cin >> n >> k;
        bath.push_back(1);
        for(long long i=1; i<=n; i++){
            bath.push_back(0);
        }
        bath.push_back(1);
        //for(long long i=0; i<bath.size(); i++){
        //    cout << bath[i] << " ";
        //}
        //cout << endl;
        for(long long i=1; i<=k; i++){
            findpos(n);
        }

        cout << "Case #" << tc << ": " << max(finalls, finalrs)-1 << " " << min(finalls, finalrs)-1 << endl;
        //cerr << "Case #" << tc << ": " << max(finalls, finalrs)-1 << " " << min(finalls, finalrs)-1 << endl;

    }
}
