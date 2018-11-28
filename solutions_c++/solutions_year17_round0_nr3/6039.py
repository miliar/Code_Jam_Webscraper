//
// Created by Harsh Mathur on 08/04/17.
//

#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <math.h>


using namespace std;

struct points{
    unsigned long long int left;
    unsigned long long int right;
};

typedef struct points points;

bool cmp_points(points point1, points point2) {
    unsigned long long int len2, len1;
    len2 = point2.right - point2.left;
    len1 = point1.right - point1.left;
    if (len1 < len2) {
        return true;
    } else if (len1 == len2) {
        return point1.left > point2.left;
    } else {
        return false;
    }
}

void find_out_ls_rs(unsigned long long int n, unsigned long long int k, int t) {
    unsigned long long int i = 1, min_d=0, max_d=0;
    vector<points> spaces;
    points point;
    point.left = 0;
    point.right = n+1;
    spaces.push_back(point);
    make_heap(spaces.begin(), spaces.end(), cmp_points);

    for (i=1;i<=k; i++) {
        unsigned long long int index = 0;
        pop_heap(spaces.begin(), spaces.end(), cmp_points);
        points for_me = spaces.back();
        spaces.pop_back();
        unsigned long long int no_of_elements = for_me.right - for_me.left - 1;
        if (no_of_elements%2 == 0) {
            index = (no_of_elements-1)/2;
        }
        else {
            index = no_of_elements/2;
        }
        index = index + for_me.left + 1;
        points point1, point2;
        point1.left = for_me.left;
        point1.right = index;
        point2.left = index;
        point2.right = for_me.right;
        min_d = min(index - for_me.left - 1, for_me.right - index - 1);
        max_d = max(index - for_me.left - 1, for_me.right - index - 1);
        spaces.push_back(point1);
        push_heap(spaces.begin(), spaces.end(), cmp_points);
        spaces.push_back(point2);
        push_heap(spaces.begin(), spaces.end(), cmp_points);
    }

    cout<<"Case #"<<t<<": "<<max_d<<" "<<min_d<<endl;
}

int main() {
    int t;
    cin>>t;
    unsigned long long int n, k;
    int i = 1;
    while (t--) {
        cin>>n>>k;
        find_out_ls_rs(n, k, i);
        i++;
    }
    return 0;
}