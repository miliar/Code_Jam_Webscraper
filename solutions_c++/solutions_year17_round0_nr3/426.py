#include <iostream>
#include <map>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int c=1; c<=T; c++) {
    unsigned long long K, N;
    cin >> N >> K;

    map<unsigned long long, unsigned long long> slots;

    unsigned long long last = N;
    slots[N] = 1;

    while (K>0) {
      last = (--slots.end())->first; // max slot
      long long available = slots[last];
      if (available<=K) 
	slots.erase(last);
      else
	slots[last] = slots[last] - K, available = K;

      unsigned long long left = last/2, right = (last-1)/2;

      slots[left] += available;
      slots[right] += available;

      //      cout << available << " x " << last << " -> " << left << " " << right << endl;
      
      K -= available;
    };
    
    cout << "Case #" << c << ": " << last/2 << " " << (last-1)/2 << endl; 
  };
};
