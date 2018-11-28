#include <stdio.h>
#include <math.h>
#include <vector>
#define MAX_SIZE 130

using namespace std;

struct block{
    unsigned long long len;
    unsigned long long quantity;
    bool used;
};

vector<block> block_record[MAX_SIZE];

long long T, N, K;

void add_new_block(int index, block new_block){
    //printf("Add level:%d\n", index);
    //printf("Add len:%lld\n", new_block.len);
    for(int i = 0; i < block_record[index].size(); i++){
        if(block_record[index][i].len == new_block.len){
            block_record[index][i].quantity += new_block.quantity;
            return;
        }
    }
    block_record[index].push_back(new_block);
}

block find_max_block(int index){
    unsigned long long len = 0;
    int result_index;
    for(int i = 0; i < block_record[index].size(); i++){
        if(block_record[index][i].len > len && !block_record[index][i].used){
            len = block_record[index][i].len;
            result_index = i;
        }
    }
    block_record[index][result_index].used = true;
    return block_record[index][result_index];
}

void calc(){
    unsigned long long temp = 1;
    int k = 0;
    while(temp < K){
        temp *= 2;
        k++;
    }
    int up = k;
    if(temp == K)
        up++;
    //printf("Level:%d\n", up);

    for(int i = 0; i <= up; i++)
        block_record[i].clear();

    block init_block;
    init_block.len = N;
    init_block.quantity = 1;
    init_block.used = false;
    block_record[0].push_back(init_block);

    for(int i = 1, temp = 1; i < up; i++, K-=temp, temp *= 2){
        for(int j = 0; j < block_record[i - 1].size(); j++){
            block new_block;
            new_block.quantity = block_record[i - 1][j].quantity;
            new_block.used = false;
            if(block_record[i - 1][j].len % 2 == 0){
                new_block.len = block_record[i - 1][j].len / 2;
                add_new_block(i, new_block);
                new_block.len = block_record[i - 1][j].len / 2 - 1;
                add_new_block(i, new_block);
            }else{
                new_block.len = block_record[i - 1][j].len / 2;
                new_block.quantity *= 2;
                add_new_block(i, new_block);
            }
        }
    }
    block max_block;
    while(K > 0){
        max_block = find_max_block(up - 1);
        K -= max_block.quantity;
    }
    long long left_max = max_block.len / 2;
    long long right_max = max_block.len / 2;
    if(max_block.len % 2 == 0)
        left_max--;
    printf("%lld %lld\n", right_max, left_max);
}

int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%lld%lld", &N, &K);
        printf("Case #%d: ", t);
        calc();
    }
    return 0;
}
