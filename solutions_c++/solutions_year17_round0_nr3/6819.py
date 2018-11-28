#include <iostream>
#include <vector>

using namespace std;



struct stall{
    bool oc;
    int Ls;
    int Rs;
    int minLR;
    int maxLR;
};

void printS(vector<stall>& S, int N);
void calcLRs(vector<stall>& S, int N);
void printS_alldetails(vector<stall>& S, int N);
vector<int> selectMaxOfMins(vector<stall>& S);
vector<int> selectMaxOfMaxs(vector<stall>& S, vector<int> selStalls);
void  occupyStall(vector<stall>& S, int sNum);

int main()
{
    int t,N,K;
    vector<stall> S;

    cin >> t;
    for (int cas =1 ; cas<=t; ++cas){
            cin >> N;
            cin >> K;

            //initialize
            S.clear();
            stall cS;
            cS.oc = true;
            cS.Ls = -1;
            cS.Rs = -1;
            cS.maxLR = -1;
            cS.minLR = -1;
            S.push_back(cS);
            for (int i = 1; i<=N;i++){
                 cS.oc = false;
                 S.push_back(cS);
            }
            cS.oc = true;
            S.push_back(cS);

            int lastS= -1;

            for(int k = 1; k<=K;k++){
                vector<int> selStallNumbers;
                selStallNumbers.clear();
                calcLRs(S,N);
                selStallNumbers = selectMaxOfMins(S);

                if (selStallNumbers.size()!=1){
                        selStallNumbers = selectMaxOfMaxs(S,selStallNumbers);
                }
                lastS = selStallNumbers.front();

                if (k == K){
                    cout<<"Case #"<<cas<<": "<<S[lastS].maxLR<<" "<<S[lastS].minLR<<endl;
                }
                occupyStall(S, lastS);

            }

    }
    return 0;
}

void printS(vector<stall>& S, int N){
    cout<<"|";
    for (int i = 0; i<=N+1;i++){
        cout<<S[i].oc<<"|";
    }
    cout<<endl;
}

void printS_alldetails(vector<stall>& S, int N){
    for (int i = 0; i<=N+1;i++){
        cout<<"Stall #"<<i<<"("<<S[i].oc<<") - R:"<<S[i].Rs<<" L:"<<S[i].Ls<<" Min:"<<S[i].minLR<<" Max:"<<S[i].maxLR<<endl;
    }
}

void calcLRs(vector<stall>& S, int N){
    for (int i = 0; i<=N+1;i++){
        if(!S[i].oc){
            for(int r=0; (r+i) <= N+1 ; r++){
                if(S[i+r+1].oc){
                    S[i].Rs=r;
                    break;
                }
            }
            for(int l=0; (i-l)>0; l++){
                if(S[i-l-1].oc){
                    S[i].Ls=l;
                    break;
                }
            }
            S[i].minLR = min(S[i].Ls,S[i].Rs);
            S[i].maxLR = max(S[i].Ls,S[i].Rs);
        }
    }
}

vector<int> selectMaxOfMins(vector<stall>& S){

    vector<int> sel;
    sel.clear();

    int MaxVal = S[0].minLR;
    for(unsigned int i = 1; i < S.size(); i++){
        if(S[i].minLR > MaxVal){
            MaxVal = S[i].minLR;
        }
    }
    for(unsigned int i = 0; i < S.size(); i++){
        if(S[i].minLR == MaxVal){
            sel.push_back(i);
        }
    }
    return sel;
}

vector<int> selectMaxOfMaxs(vector<stall>& S, vector<int> selStallNumbers){

    vector<int> sel;
    sel.clear();



    int MaxVal = S[selStallNumbers[0]].maxLR;

    for(unsigned int a =0; a < selStallNumbers.size(); a++){
            if(S[selStallNumbers[a]].maxLR > MaxVal){
            MaxVal = S[selStallNumbers[a]].maxLR;
        }
    }

    for(unsigned int a =0; a < selStallNumbers.size(); a++){
        if(S[selStallNumbers[a]].maxLR == MaxVal){
            sel.push_back(selStallNumbers[a]);
        }
    }
    return sel;
}

void  occupyStall(vector<stall>&S, int sNum){
    S[sNum].oc = true;
    S[sNum].Ls = -1;
    S[sNum].Rs = -1;
    S[sNum].minLR = -1;
    S[sNum].maxLR = -1;
}
