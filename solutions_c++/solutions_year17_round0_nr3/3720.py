#include <iostream>
#include <cstdlib>
#include <set>
using namespace std;

struct Empty_Stalls {
	Empty_Stalls(long long b, long long l) noexcept : begin(b), length(l) {}
	long long begin, length;
};

bool lt_op(const Empty_Stalls& lhs, const Empty_Stalls& rhs) {
	if(lhs.length == rhs.length)
		return lhs.begin < rhs.begin;
	else
		return lhs.length > rhs.length;
}

int main() {
	int T;
	cin >>T;

	for(int t = 1; t <= T; ++t) {
		long long N_stalls, K_people;
		cin >>N_stalls >>K_people;

		set<Empty_Stalls, decltype(lt_op)*> empty_stalls(lt_op);
		empty_stalls.emplace(0, N_stalls);

		/*for(auto iter = empty_stalls.begin(); iter != empty_stalls.end(); ++iter)
			cout <<iter -> begin <<" " <<iter -> length <<" / ";
		cout <<endl;*/

		for(int k = 0; k < K_people - 1; ++k) {
			auto ES_iter = empty_stalls.begin();
			
			if(ES_iter->length == 1)
				empty_stalls.erase(ES_iter);
			else if(ES_iter->length == 2) {
				long long new_begin = ES_iter->begin + 1;
				empty_stalls.erase(ES_iter);
				empty_stalls.emplace(new_begin, 1);
			}
			else {
				long long occupy_index = ES_iter->length % 2 == 1 ? ES_iter->length / 2 : ES_iter->length / 2 - 1;
				long long ori_begin = ES_iter->begin, r_new_length = ES_iter->length - occupy_index - 1;

				empty_stalls.erase(ES_iter);
				empty_stalls.emplace(ori_begin + occupy_index + 1, r_new_length);
				empty_stalls.emplace(ori_begin, occupy_index);
			}

			/*for(auto iter = empty_stalls.begin(); iter != empty_stalls.end(); ++iter)
				cout <<iter -> begin <<" " <<iter -> length <<" / ";
			cout <<endl;

			cout <<"check_1 "<<k +1<<endl;*/
		}

		auto ES_iter = empty_stalls.begin();
		//cout <<"check_2"<<endl;
		long long occupy_index = ES_iter->length % 2 == 1 ? ES_iter->length / 2 : ES_iter->length / 2 - 1;
		//cout <<"check_3"<<endl;
		long long LS = occupy_index, RS = ES_iter->length - occupy_index - 1;
		cout <<"Case #" <<t <<": " <<(LS >= RS ? LS : RS) <<" " <<(LS >= RS ? RS : LS) <<endl;	
	}

	return 0;
}