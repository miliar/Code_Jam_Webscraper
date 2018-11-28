#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
        int tests; cin >> tests;
        for(int test = 0; test<tests; ++test) {
                int n, p; cin >> n >> p;
                int total = 0, temp;
                vector<int> array;
                for(int i = 0; i<n; ++i) {
                        cin >> temp;
                        if(temp % p == 0) {total++;}
                        else{array.push_back(temp%p);}
                }

                int nums[5];
                for(int i = 0; i<5; ++i) {nums[i] = 0;}
                if(p == 2) {
                        total += (array.size()+1)/2;
                }
                else if(p == 3) {
                        for(int i = 0; i<array.size(); ++i) {
                                nums[array[i]]++;
                        }
                        while(nums[1]>0 && nums[2]>0) {
                                nums[1]--;
                                nums[2]--;
                                total++;
                        }
                        while(nums[1] > 3) {
                                nums[1] -= 3;
                                total++;
                        }
                        while(nums[2] > 3) {
                                nums[2] -= 3;
                                total++;
                        }

                        total += (nums[1] > 0) || (nums[2] > 0);
                }
                else {
                        for(int i = 0; i<array.size(); ++i) {
                                nums[array[i]]++;
                        }
                        while(nums[1]>0 && nums[3]>0) {
                                nums[1]--;
                                nums[3]--;
                                total++;
                        }
                        while(nums[2] >= 2) {
                                nums[2] -= 2;
                                total++;
                        }

                        while(nums[1] >= 2 && nums[2] > 0) {
                                nums[1] -= 2;
                                nums[2]--;
                                total++;
                        }
                        while(nums[3] >= 2 && nums[2] > 0) {
                                nums[3] -= 2;
                                nums[2]--;
                                total++;
                        }


                        while(nums[1] > 4) {
                                nums[1] -= 4;
                                total++;
                        }
                        while(nums[3] > 4) {
                                nums[3] -= 4;
                                total++;
                        }

                        total += (nums[1] > 0) || (nums[2] > 0) || (nums[3] > 0);
                }


                cout << fixed << setprecision(24) << "Case #" << test+1 << ": " << total << endl;
        }
}
