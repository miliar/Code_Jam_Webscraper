#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#define MAX_SIZE 1005
#define HASH_SIZE 1000007

using namespace std;

int T, K, len;

vector<bool*> hash_table[HASH_SIZE];
queue<bool*> bfs_queue;
queue<int> step_queue;

int hash_value(bool* array){
    int k = 1;
    int result = 0;
    for(int i = 0; i < len; i++){
        result += (array[i] * k);
        result %= HASH_SIZE;
        k *= 2;
        k %= HASH_SIZE;
    }
    return result;
}

bool is_equal(bool* a1, bool* a2){
    for(int i = 0; i < len; i++){
        if(a1[i] != a2[i])
            return false;
    }
    return true;
}

bool to_hash_table(bool* array){
    int index = hash_value(array);
    for(int i = 0; i < hash_table[index].size(); i++){
        if(is_equal(array, hash_table[index][i]))
            return false;
    }
    hash_table[index].push_back(array);
    return true;
}

void clear_hash_table(){
    for(int i = 0; i < HASH_SIZE; i++){
        for(int j = 0; j < hash_table[i].size(); j++)
            delete hash_table[i][j];
        hash_table[i].clear();
    }
}

int bfs(){
    bool end[MAX_SIZE];
    for(int i = 0; i < len; i++)
        end[i] = true;
    while(!bfs_queue.empty()){
        bool* current_state = bfs_queue.front();
        int current_step = step_queue.front();
        if(is_equal(current_state, end))
            return current_step;
        for(int i = 0; i < len - K + 1; i++){
            bool* temp = new bool[len];
            memcpy(temp, current_state, sizeof(bool) * len);
            for(int j = i; j < i + K; j++)
                temp[j] = true - temp[j];
            if(to_hash_table(temp)){
                bfs_queue.push(temp);
                step_queue.push(current_step + 1);
            }else{
                delete temp;
            }
        }
        bfs_queue.pop();
        step_queue.pop();
    }
    return -1;
}

int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        while(!bfs_queue.empty()){
            bfs_queue.pop();
            step_queue.pop();
        }
        clear_hash_table();
        char expr[MAX_SIZE];
        scanf("%s%d", expr, &K);
        len = strlen(expr);
        bool* start = new bool[len];
        for(int i = 0; i < len; i++){
            switch(expr[i]){
                case '+':
                    start[i] = true;
                    break;
                case '-':
                    start[i] = false;
                    break;
            }
        }
        bfs_queue.push(start);
        step_queue.push(0);
        int ans = bfs();
        printf("Case #%d: ", t);
        if(ans < 0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}
