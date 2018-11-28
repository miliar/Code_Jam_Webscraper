#include <bits/stdc++.h>
using namespace std;
char except(char a, char b){
   vector<char> v = {'R', 'Y', 'B'} ;
   for(auto it = v.begin() ; it != v.end(); ++it)
       if(*it == a){
           v.erase(it);
           break;
       }
   for(auto it = v.begin() ; it != v.end(); ++it)
       if(*it == b){
           v.erase(it);
           break;
       }
   return v[0];
}
void Solve(){
    map<char, int> mp;
    int N;
    int R, O, Y, G, B, V;
    scanf("%d", &N);
    scanf("%d%d%d%d%d%d", &R, &O, &Y, &G, &B, &V);
    mp['R'] = R;
    mp['O'] = O;
    mp['Y'] = Y;
    mp['G'] = G;
    mp['B'] = B;
    mp['V'] = V;
    deque<char> OO, GG, VV;
    for(int i = 0 ; i < O ; i++)
        OO.push_back('O'), OO.push_back('B'), mp['B']--;
    if(mp['B'] < 0){
        puts("IMPOSSIBLE");
        return;
    }
    if(mp['B'])OO.push_front('B'), mp['B']--;

    for(int i = 0 ; i < G ; i++)
        GG.push_back('G'), GG.push_back('R'), mp['R']--;
    if(mp['R'] < 0){
        puts("IMPOSSIBLE");
        return;
    }
    if(mp['R'])GG.push_front('R'), mp['R']--;

    for(int i = 0 ; i < V ; i++)
        VV.push_back('V'), VV.push_back('Y'), mp['Y']--;
    if(mp['Y'] < 0){
        puts("IMPOSSIBLE");
        return;
    }
    if(mp['Y'])VV.push_front('Y'), mp['Y']--;
    vector<deque<char>> LL;
    if(OO.size())LL.push_back(OO);
    if(GG.size())LL.push_back(GG);
    if(VV.size())LL.push_back(VV);
    if((int)LL.size() == 1){
        if(LL[0].front() == LL[0].back()){
            puts("IMPOSSIBLE");
            return;
        }
        for(char c : LL[0])
            printf("%c", c);
        puts("");
        return;
    }else if((int)LL.size() == 2){
        if(LL[0].front() != LL[0].back() || LL[1].front() != LL[1].back()){
            puts("IMPOSSIBLE");
            return;
        }
        deque<char> M1;
        char a = LL[0].front(), b = LL[1].front();
        if(mp[a] != mp[b]){
            puts("IMPOSSIBLE");
            return;
        }
        char m = except(a, b);
        if(mp[m])M1.push_back(m), mp[m]--;
        for(int i = 0 ; i < mp[a] ; i++){
            M1.push_back(b);
            if(mp[m])M1.push_back(m), mp[m]--;
            M1.push_back(a);
            if(mp[m])M1.push_back(m), mp[m]--;
        }
        if(mp[m] > 1){
            puts("IMPOSSIBLE");
            return;
        }
        for(char c : LL[0])
            printf("%c", c);
        for(char c : M1)
            printf("%c", c);
        for(char c : LL[1])
            printf("%c", c);
        if(mp[m])printf("%c", m);
        puts("");
    }else{
        if(LL[0].front() != LL[0].back() || LL[1].front() != LL[1].back() || LL[2].front() != LL[2].back()){
            puts("IMPOSSIBLE");
            return;
        }
        deque<char> M1, M2, M3;
        int a = LL[0].front(), b = LL[1].front(), c = LL[2].front();
        int ab = min(mp[a], mp[b]);
        //printf("ab %d\n", ab);
        mp[a] -= ab, mp[b] -= ab;
        //if(mp[c])M1.push_back(c), mp[c]--;
        for(int i = 0 ; i < ab ; i++){
            M1.push_back(b);
            //if(mp[c])M1.push_back(c), mp[c]--;
            M1.push_back(a);
            //if(mp[c])M1.push_back(c), mp[c]--;
        }
        int bc = min(mp[b], mp[c]);
        //printf("bc %d\n", bc);
        mp[b] -= bc, mp[c] -= bc;
        //if(mp[a])M2.push_back(a), mp[a]--;
        for(int i = 0 ; i < bc ; i++){
            M2.push_back(c);
            //if(mp[a])M2.push_back(a), mp[a]--;
            M2.push_back(b);
            //if(mp[a])M1.push_back(a), mp[a]--;
        }
        int ca = min(mp[c], mp[a]);
        //printf("ca %d\n", ca);
        mp[c] -= ca, mp[a] -= ca;
        //if(mp[b])M3.push_back(b), mp[b]--;
        for(int i = 0 ; i < ca ; i++){
            M3.push_back(a);
            //if(mp[b])M3.push_back(b), mp[b]--;
            M3.push_back(c);
            //if(mp[b])M3.push_back(b), mp[b]--;
        }
        if(mp[c]){
            for(int i=0;i<M1.size();i++){
                if(mp[c]){
                    mp[c]--;
                    M1.insert(M1.begin() + i, c);
                    i++;
                }
            }
            if(mp[c])M1.push_back(c), mp[c]--;
        }
        if(mp[a]){
            for(int i=0;i<M2.size();i++){
                if(mp[a]){
                    mp[a]--;
                    M2.insert(M2.begin() + i, a);
                    i++;
                }
            }
            if(mp[a])M2.push_back(a), mp[a]--;
        }
        if(mp[b]){
            for(int i=0;i<M3.size();i++){
                if(mp[b]){
                    mp[b]--;
                    M3.insert(M3.begin() + i, b);
                    i++;
                }
            }
            if(mp[b])M3.push_back(b), mp[b]--;
        }
        //printf("%c %d %c %d %c %d\n", a, mp[a], b, mp[b], c, mp[c]);
        if(mp[a] != 0 || mp[b] != 0 || mp[c] != 0){
            puts("IMPOSSIBLE");
            return;
        }
        for(char c : LL[0])
            printf("%c", c);
        for(char c : M1)
            printf("%c", c);
        for(char c : LL[1])
            printf("%c", c);
        for(char c : M2)
            printf("%c", c);
        for(char c : LL[2])
            printf("%c", c);
        for(char c : M3)
            printf("%c", c);
        puts("");
    }





    //if((B <= O && O && R * G) || (R <= G && G && O * V) || (Y <= V && V && O * G)){
        //puts("IMPOSSIBLE1");
        //return;
    //}
    //if(O && R * G)
        //B -= O + 1;
    //if(G && O * V)
        //R -= G + 1;
    //if(V && O * G)
        //Y -= V + 1;
    //int OG, GV, VO;
    //OG = min(B, R);
    //B -= OG, R -= OG;
    //GV = min(R, Y);
    //R -= GV, Y -= GV;
    //VO = min(Y, B);
    //Y -= VO, B -= VO;
    //printf("%d %d %d %d %d %d\n", OG, Y, GV, B, VO, R);
    //if((2 * OG + 1 < Y) || (2 * GV + 1 < B) || (2 * VO + 1 < R)){
        //puts("IMPOSSIBLE2");
        //return;
    //}
    //for(int i = 0 ; i < O ; i++)
        //printf("BO");
    //printf("B");
    //if(Y) printf("Y"), Y--;
    //for(int i = 0 ; i < OG ; i++){
        //printf("R");
        //if(Y) printf("Y"), Y--;
        //printf("B");
        //if(Y) printf("Y"), Y--;
    //}
    //for(int i = 0 ; i < G ; i++)
        //printf("RG");
    //printf("R");
    //if(B) printf("B"), B--;
    //for(int i = 0 ; i < GV ; i++){
        //printf("Y");
        //if(B) printf("B"), B--;
        //printf("R");
        //if(B) printf("B"), B--;
    //}
    //for(int i = 0 ; i < V ; i++)
        //printf("YV");
    //printf("Y");
    //if(R) printf("R"), R--;
    //for(int i = 0 ; i < VO ; i++){
        //printf("B");
        //if(R) printf("R"), R--;
        //printf("Y");
        //if(R) printf("R"), R--;
    //}
    //puts("");
}
int main(){
    int T;
    scanf("%d", &T);
    for(int t = 1 ; t <= T ; t++){
        printf("Case #%d: ", t);
        Solve();
    }
    return 0;
}
