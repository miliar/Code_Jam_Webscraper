#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

void fill_stalls(int n, int k);

int main() {
    int t, k, n;
    cin >> t;
    
    for (int x = 1; x <= t; ++x) {     
        cin >> n >> k;
        cout << "Case #" << x << ": ";
        fill_stalls(n, k);
        cout << endl;
    }
        
    return 0;
}

struct StallCollection {
    int left, right, size;
    
    bool operator<(const StallCollection& rhs) const {
        if (size == rhs.size)
            return left > rhs.left;
        else
            return size < rhs.size;
    }
};

void fill_stalls(int n, int k) {       
    priority_queue<StallCollection> max_heap;
    max_heap.push({1, n, n});    
    
    int leftsize, rightsize;
    
    for (int i = 0; i < k; ++i) {
        StallCollection collection = max_heap.top();
        max_heap.pop();
              
        int middle = (collection.left + collection.right) / 2;
        
        leftsize = middle - collection.left;        
        if (leftsize != 0)
            max_heap.push({collection.left, middle-1, leftsize});
            
        rightsize = collection.right - middle;
        if (rightsize != 0)
            max_heap.push({middle+1, collection.right, rightsize}); 
    }
    
    cout << max(leftsize, rightsize) << " " << min(leftsize, rightsize);
}
