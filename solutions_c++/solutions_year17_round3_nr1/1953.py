#include<iostream>
#include<limits>
#include<fstream>
#include<vector>
#include<set>
#include<algorithm>
#include<inttypes.h>
using namespace std;

struct node {
  uint64_t r;
  uint64_t h;
  int index;
  node (uint64_t r, uint64_t h, int index) : r(r), h(h), index(index) {}
};

struct greater_than_r
{
    inline bool operator() (const node& struct1, const node& struct2)
    {
        return (struct1.r > struct2.r);
    }
};

struct greater_than_h
{
    inline bool operator() (const node& struct1, const node& struct2)
    {
        return (struct1.r*struct1.h  > struct2.r*struct2.h);
    }
};

int64_t topn(std::vector<node> &vec, int required, std::set<int> &top) {

    int64_t count = 0;
    for(int i = 0; i < required; i++) {
        count += ((vec[i].r)*(vec[i].h)*2);
        top.insert(vec[i].index);
    }
    return count;
}

int64_t check(std::vector<node> &vec, int required, node &n, std::set<int> &top, int64_t count) {
        std::set<int>::iterator iter = top.find(n.index);
        if (iter != top.end()) {
            return count; 
        } else {
            count += n.r*n.h*2;
            count -= vec[required - 1].r*vec[required - 1].h*2;
            return count;
        }


}

void printVector(std::vector<node> &vec) {
        int len = vec.size();
        for(int i = 0; i < len; i++) {
            cout <<  " index " << vec[i].index <<  " rad " << vec[i].r << " hegiht " << vec[i].h << endl;
        }
}


int64_t checkarea(std::vector<node> &vec, int pc_required) {

    std::vector<node> vec1(vec.begin(), vec.end());
    std::sort(vec.begin(), vec.end(), greater_than_r());
    //printVector(vec);
    std::sort(vec1.begin(), vec1.end(), greater_than_h());
    //printVector(vec1);
    std::set<int> topn_s;
    int64_t topn_count = topn(vec1, pc_required,topn_s);
    //cout <<  "my count " << topn_count << endl;

    int length = vec.size();
    int64_t min_time = INT_MIN;
    for (int i =0 ; i < length; i++) {
        int64_t test = check(vec1, pc_required, vec[i], topn_s, topn_count);
        test += vec[i].r*vec[i].r;
        if (test > min_time)
            min_time = test;
    }
    return  (min_time);
}

typedef std::numeric_limits<long double > dbl;


int main() {
    int input;
    int total_pc , pc_required;
    uint64_t pc_r, pc_h;
    std::vector<node> horse_vec;
    ifstream file("input.txt");
    file >> input;
    for (int i =0; i< input ; i++) {
        horse_vec.clear();
        file >> total_pc;
        file >> pc_required;
        for (int j =0 ; j < total_pc ; j++) {
            file >> pc_r;
            file >> pc_h;
            node n(pc_r, pc_h, j);
            horse_vec.push_back(n);
        }
        //cout << "input " << total_pc << " "  << pc_required << endl;
        long double area = (long double)checkarea(horse_vec, pc_required);
        area = 3.141592653 * area;
        std::cout << std::fixed;
        cout.precision(6);
        cout << "Case #" << i + 1 << ": "<<  " " << area <<endl;
    }
}
