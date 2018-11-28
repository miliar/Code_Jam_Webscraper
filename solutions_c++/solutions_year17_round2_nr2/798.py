#include<stdio.h>
#include<vector>

namespace {
	using std::vector;
	
	vector<char> calculate(int i1, int i2, int i3, int i4, int i5, int i6) {
		vector<char> ans;
		if (i2 == 0 && i3 == 0 && i5 == 0 && i6 == 0) {
			if (i1 == i4) {
				for (int i = 0;i < i1;++i) {
					ans.push_back('R');
					ans.push_back('G');
				}
			}
			return ans;
		}		
		if (i1 == 0 && i3 == 0 && i4 == 0 && i6 == 0) {
			if (i2 == i5) {
				for (int i = 0;i < i2;++i) {
					ans.push_back('B');
					ans.push_back('O');
				}
			}
			return ans;
		}		
		if (i1 == 0 && i2 == 0 && i4 == 0 && i5 == 0) {
			if (i3 == i6) {
				for (int i = 0;i < i3;++i) {
					ans.push_back('Y');
					ans.push_back('V');
				}
			}
			return ans;
		}
		bool red = false;
		bool blue = false;
		bool yellow = false;
		if (i2 > 0) {
			i5 -= i2;
			blue = true;
			if (i5 <= 0) return ans;
		}
		if (i4 > 0) {
			i1 -= i4;
			red = true;
			if (i1 <= 0) return ans;
		}
		if (i6 > 0) {
			i3 -= i6;
			yellow = true;
			if (i3 <= 0) return ans;
		}
		if (i1 >= i3 && i1 >= i5) {
			if (i1 > i3 + i5) return ans;
			int num = i3 + i5 - i1;
			int num_yellow = num/2;
			int num_blue = num - num_yellow;
			for (int i = 0;i < i5 - num_blue;++i) {
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}				
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
			}			
			for (int i = 0;i < i3 - num_yellow;++i) {
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}				
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}
			}
			for (int i = 0;i < num_yellow;++i) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}
			}
			if (num_blue > num_yellow) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
			}
			return ans;
		}
		if (i3 >= i1 && i3 >= i5) {
			if (i3 > i1 + i5) return ans;
			int num = i1 + i5 - i3;
			int num_red = num/2;
			int num_blue = num - num_red;
			for (int i = 0;i < i5 - num_blue;++i) {
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}				
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
			}			
			for (int i = 0;i < i1 - num_red;++i) {
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}				
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}
			}
			for (int i = 0;i < num_red;++i) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}
			}
			if (num_blue > num_red) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}
			}
			return ans;
		}
		if (i5 >= i3 && i5 >= i1) {
			if (i5 > i3 + i1) return ans;
			int num = i3 + i1 - i5;
			int num_yellow = num/2;
			int num_red = num - num_yellow;
			for (int i = 0;i < i1 - num_red;++i) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}				
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}
			}			
			for (int i = 0;i < i3 - num_yellow;++i) {
				ans.push_back('B');
				if (blue) {
					blue = false;
					for (int j = 0;j < i2;++j) {
						ans.push_back('O'); ans.push_back('B');
					}
				}				
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}
			}
			for (int i = 0;i < num_yellow;++i) {
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}
				ans.push_back('Y');
				if (yellow) {
					yellow = false;
					for (int j = 0;j < i6;++j) {
						ans.push_back('V'); ans.push_back('Y');
					}
				}
			}
			if (num_red > num_yellow) {
				ans.push_back('R');
				if (red) {
					red = false;
					for (int j = 0;j < i4;++j) {
						ans.push_back('G'); ans.push_back('R');
					}
				}
			}
			return ans;
		}

	}
}

int main(int argc, char** argv) {
	if (argc != 3) return 0;
	FILE* input;
	FILE* output;
	input = fopen(argv[1],"r");
	output = fopen(argv[2],"w");
	int t;
	fscanf(input,"%d",&t);
	for (int z = 0;z < t;++z) {
		int n;
		int i1;
		int i2;
		int i3;
		int i4;
		int i5;
		int i6;
		fscanf(input,"%d",&n);
		fscanf(input,"%d",&i1);
		fscanf(input,"%d",&i2);
		fscanf(input,"%d",&i3);
		fscanf(input,"%d",&i4);
		fscanf(input,"%d",&i5);
		fscanf(input,"%d",&i6);
		vector<char> ans = calculate(i1,i2,i3,i4,i5,i6);
		if (ans.size() == 0) {
			fprintf(output,"Case #%d: IMPOSSIBLE\n",z+1);
		}
		else {
			fprintf(output,"Case #%d: ",z+1);
			for (int i = 0;i < ans.size();++i) {
				fprintf(output,"%c",ans[i]);
			}
			fprintf(output,"\n");
		}
	}
}
