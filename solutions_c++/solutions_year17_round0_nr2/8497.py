#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int i=0; i<t; ++i) {
		std::string num;
		cin >> num;

		while (true)
        {
            bool modified = false;
            for (int j = 0; j < num.length() - 1; j++) {
                if (num[j] > num[j+1]) {
                    num[j]--;
                    for (int k = j+1; k < num.length(); k++)
                        num[k] = '9';

                    if (num[0] == '0' && num.length() > 1)
                        num = num.erase(0, 1);

                    modified = true;
                    break;
                }
            }

            if (!modified)
                break;
        }

		std::cout << "Case #" << (i + 1) << ": " << num << std::endl;
	}
}