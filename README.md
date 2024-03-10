KeeLoq Remote
for use with Flipper Zero


/key {
  clear
  echo Keeloq Flipper Zero Generator
  echo ---
  if $exists(KEELOQ/key.txt) == $false { echo  key.txt not found | HALT }
  set %read.count 1
  set %write.count 1
  set %read.total $lines(KEELOQ/key.txt)
  echo total keys: %read.total
  :writekey
  if ($len($read(KEELOQ/key.txt,%read.count)) != 8 ) { inc %read.count 1 | echo bad key - skipping | goto writekey }
  if (%write.count <= 9) { set %write.count 0000 $+ %write.count | goto next }
  if (%write.count <= 99) { set %write.count 000 $+ %write.count | goto next }
  if (%write.count <= 999) { set %write.count 00 $+ %write.count | goto next }
  if (%write.count <= 9999) { set %write.count 0 $+ %write.count | goto next }
  :next
  set %file KEELOQ/Key $+ %write.count $+ .sub 
  set %K1 $mid($read(KEELOQ/key.txt,%read.count),1,2)
  set %K2 $mid($read(KEELOQ/key.txt,%read.count),3,2)
  set %K3 $mid($read(KEELOQ/key.txt,%read.count),5,2)
  set %K4 $mid($read(KEELOQ/key.txt,%read.count),7,2)
  write %file Filetype: Flipper SubGhz Key File
  write %file Version: 1
  write %file Frequency: 433920000
  write %file Preset: FuriHalSubGhzPresetOok270Async
  write %file Latitute: nan
  write %file Longitude: nan
  write %file Protocol: KeeLoq
  write %file Bit: 64
  write %file Key: %K1 %K2 %K3 %K4 C2 44 00 05
  write %file Manufacture: Unknown
  inc %read.count 1
  inc %write.count 1
  if %read.count == %read.total { echo finished | HALT }
  echo KEY %read.count - %file Key: %K1 %K2 %K3 %K4 C2 44 00 05
  goto writekey
}

