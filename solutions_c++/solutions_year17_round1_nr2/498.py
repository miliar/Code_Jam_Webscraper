#ifndef MY_LIB_INCLUDED
#define MY_LIB_INCLUDED
#include <cstdio>

template <typename Tp>
inline void read(Tp &ret){
	ret = 0;
	int f = 1; char ch = getchar();
	for (;ch < '0' || ch > '9'; ch = getchar())
		if (ch == '-') f = -f;
	for (;'0' <= ch && ch <= '9';ch = getchar())
		ret = ret * 10 + ch - '0';
	ret *= f;
}

inline int read(){
	int ret = 0;
	read(ret);
	return ret;
}

template <typename Tp>
inline Tp Power(Tp x, long long b){
	Tp y(1);
	while (b){
		if (b & 1) y = x * y;
		x = x * x;
		b >>= 1;
	}
	return y;
}

template <typename Tp>
inline Tp Power(Tp x, int b){
	Tp y(1);
	while (b){
		if (b & 1) y = x * y;
		x = x * x;
		b >>= 1;
	}
	return y;
}

#endif
