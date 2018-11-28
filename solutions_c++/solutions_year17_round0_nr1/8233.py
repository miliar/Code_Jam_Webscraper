{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #include <iostream>\
#include <cstring>\
using namespace std;\
\
void flip_pancake( string* pancake, const int l, const int window )\
\{\
	for(int i = 0; i < window; i++)\
	\{\
		(*pancake)[i + l]  = ( (*pancake)[i + l] == '-') ? '+' : '-';\
	\}\
\}\
\
bool checkCompleted( const string pancake )\
\{\
	int pancakeSize = pancake.length();\
	for(int i = 0; i < pancakeSize; i++)\
	\{\
		if(pancake[i] == '-')\
			return false;\
	\}\
	\
	return true;\
\}\
\
int main() \{\
	int t;\
	cin >> t;\
	for( int i = 1; i <= t; i++ )\
	\{\
		string pancake;\
		int window;\
		cin >> pancake >> window;\
		int pancakeSize = pancake.length();\
		int flips = 0;\
		bool completed = false;\
		for( int l = 0; l < pancakeSize; l++ )\
		\{\
			if( pancake[l] == '-' )\
			\{\
				if( l + window <= pancakeSize )\
				\{\
					// DEBUG : cout << pancake << endl;\
					flip_pancake( &pancake, l, window );\
					// DEBUG : cout << pancake << endl;\
					flips++;\
				\}\
				else\
				\{\
					completed = false;\
					break;\
				\}\
			\}\
			else\
			\{\
				completed = checkCompleted( pancake );\
			\}\
		\}\
		\
		if( completed )\
		\{\
			cout << "Case #" << i << ": " << flips;\
		\}\
		else\
		\{\
			cout << "Case #" << i << ": " << "IMPOSSIBLE";\
		\}\
		\
		cout << endl;\
	\}\
	// your code goes here\
	return 0;\
\}}