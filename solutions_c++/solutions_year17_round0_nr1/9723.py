#include <cstdio>
#include <queue>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
#define MAX 1001
#define PLUS '+'
#define MINUS '-'

typedef struct Cake{
    string cake;
};

char cake[MAX];
int K, TC;
vector<string> visit;
FILE *output = fopen("out.txt", "w");

void init(){
    K = 0;
    visit.clear();
}

void input(){
    scanf("%s %d", cake, &K);
}

bool isVisit(string str){
    for(int i = 0, len = (int)visit.size(); i<len; i++){
        if(str == visit[i]) return true;
    }
    return false;
}

void result(int num){
    bool isFind = false;
    int cnt= 0;
    char tmpGoal[MAX];
    string start = cake;
    int len = (int)start.length();
    string goal;
    for(int i = 0; i<len; i++)
        tmpGoal[i] = PLUS;
    tmpGoal[len] = '\0';
    goal = tmpGoal;
    queue<string> q;
    q.push(cake);
    visit.push_back(cake);
    while(!q.empty()){
        int qSize = (int)q.size();
        while(qSize--){
            string c = q.front();
          //  printf("cnt(%d) : %s\n", cnt, c.c_str());
            if(c == goal){
                isFind = true;
                break;
            }
            q.pop();
            char next[MAX];
            for(int i = 0; i<len-(K-1); i++){
                for(int j = 0; j<i; j++)
                    next[j] = c.c_str()[j];
                for(int j = i; j<i+K; j++)
                    next[j] = c.c_str()[j] == PLUS ? MINUS : PLUS;
                for(int j = i+K; j<len; j++)
                    next[j] = c.c_str()[j];
                next[len] = '\0';
                string nextStr = next;
                if(!isVisit(nextStr)){
                    visit.push_back(nextStr);
                    q.push(nextStr);
                }
            }
        }
        if(isFind) break;
        cnt++;
    }
    
    if(isFind) fprintf(output,"Case #%d: %d\n",num, cnt);
    else fprintf(output, "Case #%d: IMPOSSIBLE\n", num);
}
int main(){
    
    scanf("%d", &TC);
    for(int i =1; i<=TC; i++){
        init();
        input();
        result(i);
    }
    fclose(output);
    return 0;
}
