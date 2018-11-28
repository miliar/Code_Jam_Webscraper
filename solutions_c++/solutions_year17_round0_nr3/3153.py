//
//  main.cpp
//  untitled
//
//  Created by Hardik Goyal on 4/8/17.
//  Copyright © 2017 Hardik Goyal. All rights reserved.
//

#include <functional>

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>




using namespace std;

struct element{
public:
    element(){};
    element (long long l, long long r, long long count){this->l = l; this->r = r;this->count =count;
        size = r-l+1;};
    friend bool operator==(const element& l, const element& r)
    {
        return ((l.r-l.l)==(r.r-r.l));
    };
    long long l, r;
    long long size;
    long long count;
};

struct comp{
    bool operator() (const element a, const element b){

        
        long long min_a = std::min((a.r+a.l)/2 - a.l, a.r -(a.r+a.l)/2);
        long long min_b = std::min((b.r+b.l)/2 - b.l, b.r -(b.r+b.l)/2);
        
        
        long long max_a = std::max((a.r+a.l)/2 - a.l, a.r -(a.r+a.l)/2);
        long long max_b = std::max((b.r+b.l)/2 - b.l, b.r -(b.r+b.l)/2);
        
        if (min_a == min_b){
            return max_a < max_b;
        } else{
            return min_a < min_b;
        }
    }
};

class MyQueue : public std::priority_queue<element, std::vector<element>, comp>
{
public:
    void pop(long long& coun)
    {
        auto f = top();
        coun = f.count;
        priority_queue::pop();
        
    };
    
    void push(const value_type& __v)
    {
        element x = __v;
        auto f = std::find(c.begin(), c.end(), x);
        if (f!=c.end()){
            f->count+=__v.count;
        } else{
            priority_queue::push(__v);
        }
    };

};

int main()
{
    int N;
    cin >> N;
    short p=1;
    while (N!=0)
    {
        long long n, m;
        cin >> n >> m;
        
        MyQueue pq;
        
        pq.push(element(1, n, 1));
        
        element e;
        long long l = 0, r = 0;
        while (m>0)
        {
            e = pq.top();
            
            long long num_del = 0;
            
            pq.pop(num_del);
            m-=num_del;
            
            if (e.l != e.r){
                long long mid = (e.r + e.l)/2;
            
                l = mid-e.l;
                r = e.r - mid;
                
                if (l>0){
                    pq.push(element(e.l, mid-1, num_del));
                }
                if (r>0){
                    pq.push(element(mid+1, e.r, num_del));
                }
                
            } else{
                l =0;
                r=0;
            }
        }
        
        cout << "Case #" << p << ": " << std::max (l, r) << "  " << std::min(l, r) << endl;
        
        p++;
        
        N--;
        
    }
}
