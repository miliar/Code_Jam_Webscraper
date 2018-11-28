#include <iostream>
#include <string>

int main (){

	int test_cases, count;

	std::cin >> test_cases;
	for (int i = 0; i < test_cases; i++){
		std::string nums;
		std::cin >> nums;
		std::string ans;
		char lastchar = 'a';
		size_t firstOccurrence = 0;
		for (int j = 0; j < nums.size() - 1; j++){
			if(nums[j] != lastchar){
				firstOccurrence = j;
			}
			if(nums[j] > nums[j+1]){
				if(nums[j] == '1'){
					for(int k = 0; k < nums.size() -1; k++ ){
						ans += '9';
					}
				} else {
					ans = nums.substr(0,firstOccurrence);
					ans += static_cast<char>(static_cast<int>(nums[firstOccurrence]) - 1);
					for(int k = firstOccurrence+1; k < nums.size(); k++){
						ans += '9';
					}
				}
				break;
			}
			lastchar = nums[j];
		}
		if (ans == ""){
			ans = nums;
		}
		std::cout << "Case #" << i+1 << ": " << ans <<std::endl;
	}
	
	return 0;
}