#include <iostream>
#include <cstdlib>
using std::cout;
using std::endl;

long getTiny(long num) {
    long remain = 10;
    while(1) {
        long tmp = num;
        while(tmp) {
            if (remain >= tmp % 10) {
                remain = tmp % 10;
            } else {
                remain = -1;
                break;
            }
            tmp = tmp/10;
        }
        if (remain >= 0) {
            return num;
        } else {
            num = num-1;
            remain = 10;
        }
    }
}

int main() {

    int nums = 0;
    long arr[100] = {0};

    FILE *fp = fopen("/Users/vic/Dev/Alg/CodeJam/ProblemB-TinyNumbers/B-small-attempt1.in", "r");

    fscanf(fp, "%d", &nums);
    for(int i = 0; i < nums; i ++) {
        fscanf(fp, "%d", &arr[i]);
    }

    fclose(fp);
    long res[100];
    for (int i = 0; i < nums; i ++) {
        res[i] = getTiny(arr[i]);
    }

    FILE *oFP = fopen("/Users/vic/Dev/Alg/CodeJam/ProblemB-TinyNumbers/ouput","a+");
    for(int i = 0; i < nums; i ++) {
        fprintf(oFP, "Case #%d: %ld\n", i+1, res[i]);
    }

    fclose(oFP);


    return 0;
}