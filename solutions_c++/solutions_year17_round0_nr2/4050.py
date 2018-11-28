#include<bits/stdc++.h>

bool check(std::string s) {
	int len = s.length();
	//std::cout << "check " << len << " " << s[len - 2] << " " << s[len - 1] << std::endl;
	for(int i = 0; i + 1 < len; i ++) {
		if(s[i] > s[i + 1]) {
			return false;
		}
	}
	return true;
}

void reduce(std::string &s, int index) {
	bool ok = false;
	int len = s.length();
	for(int i = index; i >= 1; i --) {
		if(s[i] >= '1') {
			s[i] --;
			ok = true;
			break;
		} else {
			s[i] = '9';
			s[i - 1] --;
		}
	}
	if(!ok) {
		s[0] --;
	}
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
	std::string str;
	int T;
	std::cin >> T;
	for(int t = 1; t <= T; t ++) {
		std::cin >> str;
		std::cout << "Case #" << t << ": ";
		int id = -1, len = str.length();
		for(int i = 0; i + 1 < len; i ++) {
			if(str[i] > str[i + 1]) {
				id = i;
				break;
			}
		}
		if(id == -1) {
			std::cout << str << std::endl;
			continue;
		}
		//std::cout << "id: " << id << std::endl;
		//std::cout << "ddd: " << check(str) << std::endl;
		for(int i = id; i >= 0; i --) {
			if(!check(str)) {
				//std::cout <<"han " << i << " " << str << std::endl;
				reduce(str, i);
				str[i + 1] = '9';
			} else {
				break;
			}
		}
		for(int i = id + 1; i < len; i ++) {
			str[i] = '9';
		}
		//std::cout << "wahaha " << str << std::endl;
		long long ans = 0;
		for(int i = 0; i < len; i ++) {
			ans = 10 * ans + (str[i] - '0');
		}
		std::cout << ans << std::endl;
	}
	return 0;
}
